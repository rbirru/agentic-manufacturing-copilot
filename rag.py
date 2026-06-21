from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

DB_DIR = "chroma_db"

def get_retriever():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 2})

def retrieve_context(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [doc.metadata for doc in docs]

    return context, sources