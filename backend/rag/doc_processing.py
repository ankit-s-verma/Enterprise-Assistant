from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentLoader:
    def __init__(self, knowledge_base_path: str = "app/knowledge_base"):
        self.knowledge_base = Path(knowledge_base_path)

    def load_documents(self) -> list[Document]:
        if not self.knowledge_base.exists():
            raise FileNotFoundError(f"Knowledge base not found: {self.knowledge_base.resolve()}")

        all_docs: List[Document] = []

        pdf_files = sorted(self.knowledge_base.rglob("*.pdf"))

        if not pdf_files:
            return "No PDF files found in the knowledge base."

        for pdf_path in pdf_files:
            try:
                loader = PyPDFLoader(str(pdf_path))
                documents = loader.load()

                category = pdf_path.parent.name

                for index, doc in enumerate(documents):
                    doc.metadata.update(
                        {
                            "filename" : pdf_path.name,
                            "category": category,
                            "page_number" : index + 1
                        }
                    )
                all_docs.extend(documents)

            except Exception as e:
                return "Failed to load {pdf_path.name}: {e}"

        return all_docs

class DocumentSplitter:
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 150):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                            chunk_overlap=chunk_overlap,
                                                            separators=["\n\n", "\n", ".", " ", ""]
                                                            )
        
    def split_doc(self, documents: List[Document]) -> List[Document]:
        if not documents:
            print("No documents available for splitting")
            return []
        
        chunks = self.text_splitter.split_documents(documents)
        for index, chunk in enumerate(chunks, start=1):
            filename = chunk.metadata["filename"]
            page = chunk.metadata["page_number"]

            chunk.metadata["chunk_id"] = (
                f"{filename}_Page{page}_Chunk{index}"
            )
        return chunks