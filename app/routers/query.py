from fastapi import APIRouter
from app.services.qa import answer_question

router = APIRouter(prefix="/query", tags=["RAG"])

@router.post("/")
def query(question: str):
    return answer_question(question)
