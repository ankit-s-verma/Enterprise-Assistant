from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "backend" / "rag" / "models" / "all-MiniLM-L6-v2"
KNOWLEDGE_BASE_PATH = PROJECT_ROOT / "knowledge_base"
CHROMA_DB_PATH = PROJECT_ROOT / "chroma_db"
COLLECTION_NAME = "enterprise_knowledge"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 4