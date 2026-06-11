from qdrant_client import QdrantClient
from qdrant_client.http import models as m

client = QdrantClient(url="http://localhost:6333")

COLLECTION = "lawfirm_cases"

def init_collection(vector_size=384):
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION not in names:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=m.VectorParams(
                size=vector_size,
                distance=m.Distance.COSINE
            )
        )
