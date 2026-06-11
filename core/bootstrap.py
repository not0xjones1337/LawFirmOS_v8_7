from core.logger import log
from services.qdrant_service import QdrantService
from services.ingestion_service import IngestionService
from services.ai_service import AIService
from app.case_manager import CaseManager
from app.drafting_engine import DraftingEngine

def boot_system():
    case_manager = CaseManager()
    case_manager.create_case ("CASE_001", "Default Case")

    log("BOOT: Case system initialized")

    drafting = DraftingEngine()
    qdrant = QdrantService()
    ingestion = IngestionService(qdrant)
    ai = AIService()

    log("BOOT: RAG system ready")

    return True, {
    "qdrant": qdrant,
    "ingestion": ingestion,
    "ai": ai,
    "case_manager": case_manager,
    "drafting": drafting
}
