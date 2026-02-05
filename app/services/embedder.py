import json
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

PROCESSED_DIR = Path("data/processed")
VECTOR_DIR = Path("data/vectorstore")
VECTOR_DIR.mkdir(parents=True, exist_ok=True)

def ingest_documents():
    texts = []
    metadatas = []

    for file in PROCESSED_DIR.glob("*.json"):
        data = json.load(open(file, "r", encoding="utf-8"))[0]

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_text(data["text"])

        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({
                "document_id": data["document_id"],
                "file_name": data["file_name"]
            })

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    vectorstore.save_local(VECTOR_DIR)

    return {
        "documents_indexed": len(set(m["document_id"] for m in metadatas)),
        "total_chunks": len(texts)
    }
