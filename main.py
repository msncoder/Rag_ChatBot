from Retrieval.retriever import retrieve_chunks
from Retrieval.prompt import build_prompt
from Retrieval.llm import generate_answer


def main():

    print("RAG chatbot started. Type 'exit' to stop.\n")

    while True:

        query = input("You: ").strip()

        if query.lower() in ["exit", "quit"]:
            break

        if not query:
            continue

        # 1. Retrieve chunks
        chunks = retrieve_chunks(query, k=3)

        # DEBUG
        print("\n========== RETRIEVED CHUNKS ==========\n")

        for i, doc in enumerate(chunks, 1):
            print(f"\n--- CHUNK {i} ---")
            print(doc.page_content[:1000])
            print("\nMETADATA:")
            print(doc.metadata)

        print("\n======================================\n")

        # 2. Build prompt
        prompt = build_prompt(query, chunks)

        # DEBUG
        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n============================\n")

        # 3. Generate answer
        answer = generate_answer(prompt)

        print("\nAssistant:", answer)
        print("\n" + "-" * 80 + "\n")


if __name__ == "__main__":
    main()