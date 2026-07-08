import json
import time
from groq import Groq
from app.core.configure import settings
from app.llm.client import LLMClient
from app.llm.prompts import get_general_assistant_system_prompt, get_intent_classification_system_prompt, get_rag_prompt
from app.rag.knowledge_service import knowledge_service

RAG_KEYWORDS = [
    "policy",
    "leave",
    "vpn",
    "benefits",
    "holiday",
    "work from home",
    "password",
    "employee handbook",
    "hardware"
]

class LLMService:

    def __init__(self):
        self.client: Groq = LLMClient.get_client()
        self.model = settings.LLM_MODEL    

    def _chat_completion(self, messages: list[dict[str, str]]) -> str:
        start = time.perf_counter()
        response = self.client.chat.completions.create(
            model = self.model,
            messages=messages,
            temperature=settings.LLM_TEMPERATURE
        )

        return response.choices[0].message.content


    def classify_intent(self, question: str, conversation_history: list[dict[str, str]] | None = None) -> dict:

        system_prompt = get_intent_classification_system_prompt()

        messages = [
            {
                "role" : "system",
                "content" : system_prompt
            }
        ]

        if conversation_history:
            messages.extend(conversation_history)
        else:
            messages.append(
                {
                    "role" : "user",
                    "content" : question
                }
            )
        response = self._chat_completion(messages)


        raw_response = response.strip()

        if raw_response.startswith("```json"):
            raw_response = raw_response.replace("```json","")

        if raw_response.startswith("```"):
            raw_response = raw_response.replace("```","")

        return json.loads(raw_response.strip())
    
    def answer_question(self, question: str, conversation_history: list[dict[str,str]] | None = None) -> str:

        if self.should_use_rag(question):
            context = knowledge_service.retrieve_context(question)

            if context:
                system_prompt = get_rag_prompt(context, question)

            else:
                system_prompt = get_general_assistant_system_prompt(question)

        else:
            system_prompt = get_general_assistant_system_prompt(question)

        messages = [
            {
                "role" : "system",
                "content" : system_prompt
            }
        ]

        if conversation_history:
            messages.extend(conversation_history)
        else:
            messages.append(
                {
                    "role" : "user",
                    "content" : question
                }
            )

        return self._chat_completion(messages)
    
    def should_use_rag(self, question: str) -> bool:
        question = question.lower()

        return any(keyword in question for keyword in RAG_KEYWORDS)