import os
from dotenv import load_dotenv

# 1. Muhit o'zgaruvchilarini eng birinchi yuklaymiz
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore as Qdrant
from langchain_core.documents import Document
from qdrant_client import QdrantClient
from qdrant_client.http import models

# 2. Qdrant Cloud klientini sozlash
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key
)

# 3. Embeddings sozlamasi
embeddings = OpenAIEmbeddings(
    model="gemini-embedding",
    openai_api_key=os.getenv("GEMINI_API_KEY"),
    openai_api_base="https://saidazam-litellm-proxy.hf.space/v1"
)

COLLECTION_NAME = "chat_history"

# 4. Kolleksiya mavjud bo'lmasa, uni avtomatik yaratamiz
collections = [c.name for c in qdrant_client.get_collections().collections]

if COLLECTION_NAME not in collections:
    # Embedding hajmini (dimension) aniqlaymiz (gemini-embedding uchun odatda 768)
    dummy_vector = embeddings.embed_query("test")
    vector_size = len(dummy_vector)
    
    qdrant_client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )

# 5. Qdrant VectorStore ulanishi
memory_store = Qdrant(
    client=qdrant_client,
    collection_name=COLLECTION_NAME,
    embedding=embeddings
)

def save_turn_to_memory(question: str, answer: str):
    """Suhbat yakunlangach, savol va javobni Qdrant bulutiga saqlaydi."""
    turn_text = f"User Question: {question}\nAgent Answer: {answer}"
    doc = Document(page_content=turn_text, metadata={"type": "past_turn"})
    memory_store.add_documents([doc])

def get_relevant_history(question: str, k: int = 2) -> str:
    """Yangi savolga aloqador oldingi suhbatlarni Qdrant'dan topadi."""
    docs = memory_store.similarity_search(question, k=k)
    past_contexts = [doc.page_content for doc in docs if doc.metadata.get("type") == "past_turn"]
    return "\n---\n".join(past_contexts)