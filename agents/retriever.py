import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

def retrieve_docs(query: str, top_k: int = 2) -> list[str]:
    """
    Qdrant vektor bazasidan berilgan savolga eng yaqin top_k ta hujjatni topib beradi.
    """
    embeddings = OpenAIEmbeddings(
        base_url="https://saidazam-litellm-proxy.hf.space/v1",
        api_key=os.getenv("GEMINI_API_KEY"),
        model="gemini-embedding"
    )

    qdrant = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name="knowledge_base",
        path="./qdrant_db"
    )

    docs = qdrant.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]

# Agentni alohida test qilib ko'rish uchun:
if __name__ == "__main__":
    test_query = "Tizimda qanday agentlar bor?"
    results = retrieve_docs(test_query)
    print(f"🔍 Savol: {test_query}\n")
    print("📄 Topilgan natijalar:")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res}")