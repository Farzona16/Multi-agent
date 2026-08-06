import os
from dotenv import load_dotenv

# .env faylini yuklaymiz
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")
langfuse_public = os.getenv("LANGFUSE_PUBLIC_KEY")

print("--- API Keys Check ---")
print("Gemini API Key:", "✅ Topildi" if gemini_key else "❌ Topilmadi")
print("Tavily API Key:", "✅ Topildi" if tavily_key else "❌ Topilmadi")
print("Langfuse Public Key:", "✅ Topildi" if langfuse_public else "❌ Topilmadi")
    