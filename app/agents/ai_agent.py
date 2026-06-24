import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))


def perform_actions(question: str) -> dict:
    """
    Extract intent and entities from user query.
    Returns JSON object.
    """

    prompt = f"""
    You are an enterprise assistant. Analyze the user questions and return ONLY valid JSON.

    Possible questions - 
    1. EMPLOYEE_LOOKUP
    2. CREATE_TICKET
    3. TICKET_SEARCH
    4. GENERAL_QUERY

    Rules - 
    - If the user asks regarding an employee, use EMPLOYEE_LOOKUP
    - If the user asks to create or raise a ticket, use CREATE_TICKET
    - If the user asks to search for a ticket, use TICKET_SEARCH
    - Otherwise use GENERAL_QUERY

    Return JSON only
    
    Examples:

    1. User - 
    Show me the details of the employee E108

    Output - 
    {{
        "action" : EMPLOYEE_LOOKUP,
        "employee_id" : "E108"
    }}

    User:
    Create a ticket for VPN issue

    Output:
    {{
        "action":"CREATE_TICKET",
        "issue":"VPN issue"
    }}

    User:
    Search for a ticket INC-1234

    Output:
    {{
        "action":"TICKET_SEARCH",
        "ticket":"INC-1234"
    }}

    User:
    What is the company leave policy?

    Output:
    {{
        "action":"GENERAL_QUERY"
    }}

    Query:
    {question}
    """
    try:

        print("===== Gemini API Call Started for action =====")
        response = client.models.generate_content(
            model = 'gemini-2.5-flash-lite',
            contents=prompt
        )

        raw_response = response.text

        cleaned = raw_response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned.replace("```json", "")

        if cleaned.endswith("```"):
            cleaned = cleaned.replace("```", "")

        cleaned = cleaned.strip()

        return json.loads(cleaned)
    
    except Exception as e:
        print(f"Action Extraction Error: {e}")

        return {
            "error" : str(e)
        }

def answer_general_questions(question: str) -> str:
    """
    Handles non-action business questions.
    """

    prompt = f"""
    You are an enterprise HR and IT assistant. Answer the following question professionally and limit the response within 200 characters.

    Question:
    {question}
    """

    try:
        print("===== Gemini API Call Started for general question =====")
        response = client.models.generate_content(model='gemini-2.5-flash-lite', contents=prompt)

        return response.text
    
    except Exception as e:
        return f"Unable to generate content: {str(e)}"

if __name__ == "__main__":
    pass
    # print(perform_actions("Show details of employee E105"))
    # print(perform_actions("My system is broken"))
    # print(perform_actions("What is the onboarding process?"))