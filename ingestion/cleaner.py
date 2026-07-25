import re


def clean_text(text: str) -> str:

    # Multiple spaces remove
    text = re.sub(r"\s+", " ", text)

    # Leading/trailing spaces
    text = text.strip()

    return text


def clean_documents(documents):

    for doc in documents:

        doc.page_content = clean_text(
            doc.page_content
        )

    return documents


