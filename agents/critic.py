import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from state import AgentState

load_dotenv()

def critic_node(state: AgentState) -> dict:
    """
    Shakllangan javob yoki olingan ma'lumotlarni tekshiradi.
    Javob to'g'ri bo'lsa 'pass', aks holda 'revise' qaytaradi.
    """
    question = state.get("question", "")
    answer = state.get("answer", "") or state.get("code_result", "") or state.get("sql_result", "")
    revisions = state.get("revisions", 0)

    # Cheksiz halqaga tushib qolmaslik uchun maks 2 marta qayta ko'rishga ruxsat beramiz
    if revisions >= 2:
        print("⚠️ Critic: Maksimal qayta ko'rishlar soniga yetdi (revisions >= 2). Javob ma'qullandi.")
        return {"next_step": "end"}

    api_key = os.getenv("GEMINI_API_KEY")
    llm = ChatOpenAI(
        model="gemini-flash-lite",
        openai_api_key=api_key,
        openai_api_base="https://saidazam-litellm-proxy.hf.space/v1",
        temperature=0
    )

    prompt = f"""You are a strict Quality Assurance Critic. Evaluate whether the retrieved answer/result satisfies the user's question.

User Question: {question}
Agent Result: {answer}

Rules:
- Respond ONLY with 'PASS' if the result accurately and adequately answers the question.
- Respond ONLY with 'REVISE' if the answer is completely off-topic, empty, or incorrect.

Your Evaluation (PASS or REVISE):"""

    decision = llm.invoke(prompt).content.strip().upper()
    print(f"🧐 Critic qarori: {decision}")

    if "PASS" in decision:
        return {"next_step": "end"}
    else:
        return {
            "next_step": "supervisor",
            "revisions": revisions + 1
        }