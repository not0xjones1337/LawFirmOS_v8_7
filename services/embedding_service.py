from core.logger import log

class EmbeddingService:

    def __init__(self):
        log("EMBEDDINGS: Service initialized")

    def embed(self, text: str):
        # Placeholder embedding logic
        # Replace with real model later
        return [len(text)]  # simple fake embedding