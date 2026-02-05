from fastapi import FastAPI
from app.routers.upload import router as upload_router

app = FastAPI(title="Enterprise AI Assistant")

app.include_router(upload_router)

@app.get("/")
def health():
    return {"status": "running"}
from app.routers.ingest import router as ingest_router

app.include_router(ingest_router)
from app.routers.query import router as query_router

app.include_router(query_router)
