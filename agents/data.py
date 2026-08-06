import os
import sqlite3
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def query_sql(question: str) -> str:
    """
    Savolga mos SQL so'rovi yaratadi va faqat SELECT so'rovini bajaradi.
    """
    llm = ChatOpenAI(
        base_url="https://saidazam-litellm-proxy.hf.space/v1",
        api_key=os.getenv("GEMINI_API_KEY"),
        model="gemini-flash-lite",
        temperature=0
    )

    db_schema = """
    Table: sales
    Columns: year (INTEGER), revenue (REAL), expenses (REAL)
    """

    prompt = f"""You are an expert SQL generator. Convert the question to a SQLite SQL query based on this schema:
    {db_schema}

    CRITICAL RULE: Return ONLY the raw SQL query. Do NOT use markdown code blocks like ```sql. Return pure SQL string starting with SELECT.

    Question: {question}
    """

    sql_query = llm.invoke(prompt).content.strip()

    # Watch out / Read-Only xavfsizlik tekshiruvi:
    assert sql_query.lower().startswith("select"), f"Xavfsizlik taqiqlaydi! Faqat SELECT so'rovlari ruxsat etilgan: {sql_query}"

    print(f"📄 Generatsiya qilingan SQL: {sql_query}")

    # SQL so'rovini bajarish
    conn = sqlite3.connect("data/company.db")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()

    return f"SQL Result for '{sql_query}': {results}"

if __name__ == "__main__":
    test_q = "2024 va 2025 yillardagi umumiy daromad (revenue) qancha bo'lgan?"
    print(query_sql(test_q))