from pathlib import Path


def enrich_metadata(chunks):

    for index, chunk in enumerate(chunks):

        source = chunk.metadata.get(
            "source",
            "unknown"
        )

        chunk.metadata.update({

            "document_type": "pdf",

            "file_name": Path(
                source
            ).name,

            "chunk_id": index,

            "pipeline_version": "v1"
        })

    return chunks