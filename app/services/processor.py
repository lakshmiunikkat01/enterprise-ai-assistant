import uuid
import json
import datetime
import pandas as pd
import pdfplumber
from docx import Document
from pathlib import Path

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_text(file):
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join(p.text for p in doc.paragraphs)

    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def process_document(file):
    raw_text = extract_text(file)
    cleaned_text = clean_text(raw_text)

    document_id = str(uuid.uuid4())

    metadata = {
        "document_id": document_id,
        "file_name": file.filename,
        "file_type": file.filename.split(".")[-1],
        "uploaded_at": datetime.datetime.utcnow().isoformat()
    }

    df = pd.DataFrame([{
        "text": cleaned_text,
        **metadata
    }])

    output_file = OUTPUT_DIR / f"{document_id}.json"
    df.to_json(output_file, orient="records", indent=2)

    return metadata
