from langchain_core.documents import Document
from app.rag.embeddings import embedding_service
from app.rag.vector_store import vector_store
from app.rag.config import TOP_K

class Retriever:

    def retrieve(self, query: str, top_k:int = TOP_K) -> list[Document]:
        query_embedding = embedding_service.embed_query(query)
        results = vector_store.similarity_search(query_embedding=query_embedding, top_k=top_k)

        documents = []

        for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
            documents.append(Document(page_content=doc,metadata=metadata))

        return documents
    
retriever = Retriever()