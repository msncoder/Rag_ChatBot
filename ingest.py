from ingestion.pipeline import ingest_pdf


pdf_path = (
    r"C:\Users\ATK-Saad\Desktop\Titan_Class"
    r"\langchain\rag_chatbot\documents\soc.pdf"
)


vectorstore = ingest_pdf(pdf_path)


print("================================")
print("INGESTION COMPLETED")
print("================================")

print(
    "Total vectors stored:",
    vectorstore._collection.count()
)