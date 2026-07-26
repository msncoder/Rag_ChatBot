def build_prompt(query: str, chunks):
    context_parts = []

    for i, doc in enumerate(chunks, 1):
        page = doc.metadata.get("page", "unknown")
        source = doc.metadata.get("source", "unknown")

        context_parts.append(
            f"[Chunk {i} | Source: {source} | Page: {page}]\n{doc.page_content}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
    You are a helpful assistant for RAG.
    Answer only from the provided context.
    If the answer is not in the context, say: "I don't know based on the provided document."

Context:
{context}

Question:
{query}

Answer:
""".strip()

    return prompt