# Enterprise AI Assistant (RAG)

An **enterprise-grade Retrieval-Augmented Generation (RAG) AI Assistant** built using
FastAPI, FAISS, and Groq’s LLaMA models.  
The system enables organizations to upload internal documents and ask
natural-language questions with **source-backed answers**.

---

##  Features

- Upload enterprise documents (PDF, DOCX, TXT)
- Automatic text extraction & preprocessing
- Semantic chunking with overlap
- Vector embeddings using Sentence Transformers
- FAISS-based semantic search
- LLaMA-powered answers via Groq
- Source citations for enterprise trust
- Modular, production-style FastAPI backend


##  Architecture Overview


Documents (PDF / DOCX)
↓
FastAPI Upload API
↓
Text Extraction & Cleaning
↓
Chunking
↓
Embeddings (Sentence Transformers)
↓
FAISS Vector Store
↓
Semantic Retrieval
↓
Groq LLaMA 3.1
↓
Answer + Sources

---

##  Tech Stack

- **Backend:** FastAPI, Python  
- **Vector Database:** FAISS  
- **Embeddings:** HuggingFace Sentence Transformers  
- **LLM:** Groq (LLaMA 3.1)  
- **Frameworks:** LangChain  
- **Version Control:** Git & GitHub  

---

##  Project Structure
enterprise-ai-assistant/
├── app/
│ ├── routers/ # API routes
│ ├── services/ # Business logic (processing, embedding, QA)
│ ├── utils/ # Helpers & validators
│ └── models/ # Data schemas
│
├── data/
│ └── (processed & vectorstore ignored via .gitignore)
│
├── requirements.txt

---

##  How to Run Locally

pip install -r requirements.txt
uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

## Environment Variables
Set your Groq API key:
GROQ_API_KEY=your_api_key_here

## Why This Project Matters

This project demonstrates real-world enterprise AI engineering skills, including:
Building production-ready APIs
Implementing RAG pipelines
Handling large unstructured documents
Semantic search with vector databases
LLM integration with source-grounded answers
