import os
import io
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def execute_python_code(question: str) -> str:
    """
    Matematik yoki tahliliy savol bo'yicha Python kodini yaratib, uni yurgazadi.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "❌ Xato: GEMINI_API_KEY topilmadi."

    llm = ChatOpenAI(
        model="gemini-flash-lite",
        openai_api_key=api_key,
        openai_api_base="https://saidazam-litellm-proxy.hf.space/v1",
        temperature=0
    )

    prompt = f"""Write executable Python code to solve the following math or analytical task.
Print the final result using print().
CRITICAL RULE: Return ONLY pure Python code. Do NOT use markdown blocks like ```python.

Task: {question}
"""

    code = llm.invoke(prompt).content.strip()

    # Markdown bloklari tasodifan qo'shilib qolsa, tozalaymiz
    if code.startswith("```"):
        code = code.split("\n", 1)[1]
    if code.endswith("```"):
        code = code.rsplit("```", 1)[0]
    code = code.strip()

    print(f"🐍 Yaratilgan Python kodi:\n{code}\n")

    # Xavfsiz lokal REPL muhitida kodni yurgazish
    local_vars = {}
    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        exec(code, {}, local_vars)

        sys.stdout = old_stdout
        output = redirected_output.getvalue()
        return output.strip() if output else str(local_vars)
    except Exception as e:
        sys.stdout = old_stdout
        return f"Python kodi bajarilishida xato: {e}"

if __name__ == "__main__":
    test_q = "Agar daromad 750,000 va xarajat 350,000 bo'lsa, sof foyda marjasi (profit margin %) necha foiz bo'ladi?"
    print(f"📊 Natija: {execute_python_code(test_q)}")