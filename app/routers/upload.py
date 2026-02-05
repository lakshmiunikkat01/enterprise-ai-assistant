from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.processor import process_document
from app.utils.file_utils import validate_file

router = APIRouter(prefix="/upload", tags=["Documents"])

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    validate_file(file.filename)

    result = process_document(file)
    return {
        "message": "Document processed successfully",
        "document_id": result["document_id"],
        "file_name": result["file_name"]
    }
