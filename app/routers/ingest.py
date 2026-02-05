from fastapi import APIRouter
from app.services.embedder import ingest_documents

router = APIRouter(prefix="/ingest", tags=["RAG"])

@router.post("/")
def ingest():
    return ingest_documents()
