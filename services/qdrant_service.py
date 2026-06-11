from qdrant_client import QdrantClient
from core.logger import log

class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            "localhost",
            port=6333
        )
        self.connected = False
        self.storage = {}  # simple in‑memory store for now


    def connect(self):
        self.connected = True
        log("QDRANT: Connected")

    def store_document(self, doc_id, vector=None, payload=None):
        self.storage[doc_id] = {
          "vector": vector,
          "payload": payload
    }

    def search(self, query):
        if not self.connected:
            return []

        results = []

        # VERY SIMPLE MATCH SIMULATION (not real embeddings yet)
        for k, v in self.storage.items():
            if query.lower() in v.lower():
                results.append((k, v[:200]))

        log(f"QDRANT: Search returned {len(results)} results")
        return results

