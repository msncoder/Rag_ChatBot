from ingestion.loader import load_pdf
from ingestion.cleaner import clean_documents
from ingestion.structure import detect_structure
from ingestion.chunker import chunk_documents
from ingestion.metadata import enrich_metadata
from ingestion.embeddings import get_embedding_model

from langchain_chroma import Chroma


def ingest_pdf(file_path):

    # 1. Load PDF
    documents = load_pdf(file_path)

    # 2. Clean Text
    documents = clean_documents(documents)

    # 3. Detect Structure
    documents = detect_structure(documents)

    # 4. Create Chunks
    chunks = chunk_documents(documents)

    # 5. Add Metadata
    chunks = enrich_metadata(chunks)

    # 6. Load Embedding Model
    embeddings = get_embedding_model()

    # 7. Store Chunks + Embeddings in ChromaDB
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
        collection_name="soc_pdf"
    )

    return vectorstore