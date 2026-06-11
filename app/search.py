from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient("http://localhost:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION = "lawfirm"

def search(case_id, query):

    vector = model.encode(query).tolist()

    hits = client.search(
        collection_name=COLLECTION,
        query_vector=vector,
        limit=5,
        query_filter={
            "must": [
                {"key": "case_id", "match": {"value": case_id}}
            ]
        }
    )

    return "\n\n".join([h.payload["text"] for h in hits])
