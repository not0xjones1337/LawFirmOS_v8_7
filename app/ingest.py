import os
from pypdf import PdfReader
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient("http://localhost:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION = "lawfirm"

def ingest_case(case_id):

    folder = f"cases/{case_id}"

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            text = "\n".join([p.extract_text() or "" for p in PdfReader(path).pages])
        else:
            continue

        chunks = text.split(". ")

        for c in chunks:
            if len(c) < 20:
                continue

            vector = model.encode(c).tolist()

            client.upsert(
                collection_name=COLLECTION,
                points=[{
                    "id": hash(c),
                    "vector": vector,
                    "payload": {
                        "case_id": case_id,
                        "text": c
                    }
                }]
            )

    return "Ingestion complete"
