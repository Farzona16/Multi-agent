import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

def run_ingestion():
    print("⏳ Hujjatlar yuklanmoqda va bo'linmoqda...")
    
    # 1. Hujjatni yuklash
    loader = TextLoader("data/knowledge.txt", encoding="utf-8")
    docs = loader.load()

    # 2. Matnni chunk'larga bo'lish
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(docs)
    print(f"📄 Jami bo'lingan chunklar soni: {len(chunks)}")

    # 3. Ustozning Proksi serveriga ulangan OpenAIEmbeddings
    embeddings = OpenAIEmbeddings(
        base_url="https://saidazam-litellm-proxy.hf.space/v1",
        api_key=os.getenv("GEMINI_API_KEY"),
        model="gemini-embedding"
    )

    # 4. Qdrant vektor bazasiga saqlash
    print("🧠 Vektorlar Qdrant bazasiga yozilmoqda...")
    qdrant = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        path="./qdrant_db",
        collection_name="knowledge_base"
    )
    print("✅ Muvaffaqiyatli saqlandi! Qdrant bazasi tayyor.")

if __name__ == "__main__":
    run_ingestion()