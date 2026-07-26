from langchain_chroma import Chroma
from ingestion.embeddings import get_embedding_model


def get_vectorstore():
    embeddings = get_embedding_model()

    vectorstore = Chroma(
        persist_directory="./chroma_db",
        collection_name="soc_pdf",
        embedding_function=embeddings,
    )

    return vectorstore


def retrieve_chunks(query: str, k: int = 3):
    vectorstore = get_vectorstore()
    docs = vectorstore.similarity_search(query, k=k)
    return docs
