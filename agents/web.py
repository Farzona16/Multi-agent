import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def search_web(query: str) -> list[str]:
    """
    Tavily API yordamida internetdan ma'lumot qidiradi.
    """
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        print("⚠️ Tavily API key topilmadi, o'tkazib yuborilmoqda.")
        return []

    try:
        client = TavilyClient(api_key=tavily_key)
        response = client.search(query=query, max_results=2)
        results = [res["content"] for res in response.get("results", [])]
        return results
    except Exception as e:
        print(f"❌ Tavily Search xatosi: {e}")
        return []

if __name__ == "__main__":
    test_query = "LangGraph nima va u nimaga kerak?"
    results = search_web(test_query)
    print(f"🌐 Internetdan qidiruv natijasi ({test_query}):\n")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res}\n")