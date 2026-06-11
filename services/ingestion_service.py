from core.logger import log
from services.embedding_service import EmbeddingService


class IngestionService:

    def __init__(self, qdrant_service):
        self.qdrant = qdrant_service
        self.embedder = EmbeddingService()

    def chunk(self, text, size=500):
        return [text[i:i+size] for i in range(0, len(text), size)]

    def ingest_text(self, doc_id, text):

        if not text:
            return False

        chunks = self.chunk(text)

        for i, chunk in enumerate(chunks):

            vector = self.embedder.embed(chunk)

            self.qdrant.store_document(
                doc_id=f"{doc_id}_{i}",
                vector=vector,
                payload=chunk
            )

        log(f"INGEST TEXT: {doc_id} ({len(chunks)} chunks)")
        return True

    def ingest_file_text(self, file_name, text):

        return self.ingest_text(file_name, text)


