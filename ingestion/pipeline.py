from langchain_chroma import Chroma

from ingestion.loader import load_pdf
from ingestion.cleaner import clean_documents
from ingestion.structure import detect_structure
from ingestion.chunker import chunk_documents
from ingestion.metadata import enrich_metadata
from ingestion.embeddings import get_embedding_model


def ingest_pdf(file_path):

    # 1. Load
    documents = load_pdf(file_path)

    # 2. Clean
    documents = clean_documents(
        documents
    )

    # 3. Structure Detection
    documents = detect_structure(
        documents
    )

    # 4. Chunk
    chunks = chunk_documents(
        documents
    )

    # 5. Metadata
    chunks = enrich_metadata(
        chunks
    )

    # 6. Embedding Model
    embeddings = get_embedding_model()

    # 7. Store in ChromaDB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
        collection_name="pdf_documents"
    )

    return vectorstore


