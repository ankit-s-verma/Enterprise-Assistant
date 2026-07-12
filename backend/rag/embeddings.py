from typing import List
from sentence_transformers import SentenceTransformer
from backend.rag.config import MODEL_PATH

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(str(MODEL_PATH))

    def embed_docs(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        return embeddings.tolist()
    
    def embed_query(self, query:str) -> List[float]:
        embeddings = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.tolist()
    
embedding_service = EmbeddingService()