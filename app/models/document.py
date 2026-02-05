from pydantic import BaseModel

class DocumentMetadata(BaseModel):
    document_id: str
    file_name: str
    file_type: str
    uploaded_at: str
