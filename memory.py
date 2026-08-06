import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore as Qdrant
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

load_dotenv()

# Proxy orqali ishlaydigan Embeddings
embeddings = OpenAIEmbeddings(
    model="gemini-embedding",
    openai_api_key=os.getenv("GEMINI_API_KEY"),
    openai_api_base="https://saidazam-litellm-proxy.hf.space/v1"
)

# Suhbatlar tarixini saqlash uchun alohida in-memory Qdrant bazasi
memory_store = Qdrant.from_documents(
    documents=[Document(page_content="System Initialized", metadata={"role": "system"})],
    embedding=embeddings,
    location=":memory:",
    collection_name="chat_history"
)

def save_turn_to_memory(question: str, answer: str):
    """Suhbat yakunlangach, savol va javobni saqlaydi."""
    turn_text = f"User Question: {question}\nAgent Answer: {answer}"
    doc = Document(page_content=turn_text, metadata={"type": "past_turn"})
    memory_store.add_documents([doc])

def get_relevant_history(question: str, k: int = 2) -> str:
    """Yangi savolga aloqador oldingi suhbatlarni topadi."""
    docs = memory_store.similarity_search(question, k=k)
    past_contexts = [doc.page_content for doc in docs if doc.metadata.get("type") == "past_turn"]
    return "\n---\n".join(past_contexts)