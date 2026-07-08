from typing import List
import chromadb
from langchain_core.documents import Document
from app.rag.config import CHROMA_DB_PATH, COLLECTION_NAME

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)

    def add_docs(self, documents: List[Document], embeddings: List[List[float]]):
        ids = []
        metadatas = []
        texts = []

        for doc in documents:
            metadata = dict(doc.metadata)
            chunk_id = metadata['chunk_id']
            ids.append(chunk_id)
            texts.append(doc.page_content)
            metadatas.append(metadata)

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def count(self):
        return self.collection.count()
    
    def similarity_search(self, query_embedding: List[float], top_k: int = 4):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
    
    def reset(self):
        self.client.delete_collection(COLLECTION_NAME)
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)

# Singleton instance
vector_store = VectorStore()