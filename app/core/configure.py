import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Application configuration loaded from env variables
    """
    def __init__(self):
        pass

        self.DATABASE_URL: str = self._get_env("DATABASE_URL")
        self.LLM_PROVIDER: str = self._get_env("LLM_PROVIDER")
        self.LLM_API_KEY: str = self._get_env("LLM_API_KEY")
        self.LLM_MODEL: str = self._get_env("LLM_MODEL")
        self.LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", 0.2))
        self.LLM_TIMEOUT: int = int(os.getenv("LLM_TIMEOUT", 30))
        self.SECRET_KEY: str = self._get_env("SECRET_KEY")
        self.ALGORITHM: str = self._get_env("ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    @staticmethod
    def _get_env(key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable : {key}")
        return value

settings = Settings()