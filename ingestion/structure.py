import re


def detect_structure(documents):

    for doc in documents:

        text = doc.page_content

        headings = re.findall(
            r"(?m)^[A-Z][A-Za-z0-9\s]{2,50}$",
            text
        )

        # ChromaDB empty list metadata accept nahi karta
        if headings:
            doc.metadata["headings"] = ", ".join(headings)
        else:
            doc.metadata["headings"] = "No heading detected"

    return documents