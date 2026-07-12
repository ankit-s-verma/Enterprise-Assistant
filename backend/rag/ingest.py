from backend.rag.doc_processing import DocumentLoader, DocumentSplitter
from backend.rag.embeddings import embedding_service
from backend.rag.vector_store import vector_store

def main():
    loader = DocumentLoader()
    splitter = DocumentSplitter()

    documents = loader.load_documents()
    chunks = splitter.split_doc(documents)

    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding_service.embed_docs(texts)
    vector_store.add_docs(documents=chunks, embeddings=embeddings)

if __name__ == "__main__":
    main()

