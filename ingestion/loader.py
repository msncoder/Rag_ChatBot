from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from cleaner import clean_documents
from structure import detect_structure
from chunker import chunk_documents
from metadata import enrich_metadata
from embeddings import get_embedding_model
from langchain_chroma import Chroma


def load_pdf(file_path: str):
    loader = PyMuPDFLoader(file_path)

    documents = loader.load()

    return documents


documents = load_pdf(
    r"C:\Users\ATK-Saad\Desktop\Titan_Class\langchain\rag_chatbot\documents\soc.pdf" 
)
# print(len(documents))
# for doc in documents[:3]:
#     print(doc.page_content)


documents = clean_documents(documents)

# for doc in documents[:3]:
#     print(doc.page_content)

documents = detect_structure(documents)
# for doc in documents[:3]:
#     print(doc.page_content)
#     print(doc.metadata)

chunks = chunk_documents(documents)

# for chunk in chunks[:3]:
#     print(chunk.page_content)
#     print("---")

# chunks = enrich_metadata(chunks)

# # for chunk in chunks[:3]:
# #     print(chunk.metadata)


embeddings = get_embedding_model()

# vector = embeddings.embed_query(
#     "What is this document about?"
# )

# print("Vector dimensions:", len(vector))



vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",
    collection_name="soc_pdf"
)

print("Documents stored in ChromaDB!")
