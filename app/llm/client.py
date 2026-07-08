from groq import Groq
from app.core.configure import settings

class LLMClient:

    _client = None

    @classmethod
    def get_client(cls) -> Groq:
        if cls._client is None:
            cls._client = Groq(
                api_key=settings.LLM_API_KEY
            )

        return cls._client