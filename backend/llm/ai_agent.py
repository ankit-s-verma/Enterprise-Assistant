from backend.llm.service import LLMService

llm = LLMService()

def perform_actions(question: str, conversation_history: list[dict[str,str]] | None = None) -> dict:
    try:
        return llm.classify_intent(question, conversation_history=conversation_history)
    
    except Exception as e:
        return {
            "error" : str(e)
        }

def answer_general_questions(question: str, conversation_history: list[dict[str,str]] | None = None) -> str:
    try:
        return llm.answer_question(question, conversation_history)
    
    except Exception as e:
        return f"Unable to generate content: {str(e)}"