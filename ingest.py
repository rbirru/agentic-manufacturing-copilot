from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

DATA_DIR = "data"
DB_DIR = "chroma_db"

def load_documents():
    docs = []

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.endswith(".txt"):
            loader = TextLoader(path)
            docs.extend(loader.load())

        elif file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

    return docs

def ingest():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120
    )

    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    print(f"Indexed {len(chunks)} chunks into ChromaDB.")

if __name__ == "__main__":
    ingest()