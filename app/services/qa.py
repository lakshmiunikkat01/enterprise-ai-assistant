from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

VECTOR_DIR = Path("data/vectorstore")

def answer_question(question: str):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTOR_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join(d.page_content for d in docs)

    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

    prompt = f"""
You are an enterprise AI assistant.
Answer strictly using the context below.
If the answer is not found, say "Not found in document."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    sources = sorted(list({
        d.metadata.get("file_name", "unknown")
        for d in docs
    }))

    return {
        "answer": response.content,
        "sources": sources
    }
