from langchain_core.documents import Document
from app.llm.prompts import get_rag_prompt
from app.rag.embeddings import embedding_service
from app.rag.vector_store import vector_store
from app.rag.config import TOP_K

class KnowledgeService:

    def retrieve(self, query: str, top_k:int = TOP_K) -> list[Document]:
        query_embedding = embedding_service.embed_query(query)
        results = vector_store.similarity_search(query_embedding=query_embedding, top_k=top_k)

        documents = []

        for doc, metadata in zip(results['documents'][0], results['metadatas'][0]):
            documents.append(Document(page_content=doc,metadata=metadata))

        return documents

    def retrieve_context(self, question: str) -> str:
        documents = self.retrieve(question)

        if not documents:
            return None
        
        context = "\n\n".join(doc.page_content for doc in documents)

        return context

knowledge_service = KnowledgeService()