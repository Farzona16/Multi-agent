import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from state import AgentState

load_dotenv()

def supervisor_node(state: AgentState) -> dict:
    """
    Savolni tahlil qilib, uni tegishli specialist agentga yo'naltiradi (Routing).
    """
    question = state["question"]
    api_key = os.getenv("GEMINI_API_KEY")

    llm = ChatOpenAI(
        model="gemini-flash-lite",
        openai_api_key=api_key,
        openai_api_base="https://saidazam-litellm-proxy.hf.space/v1",
        temperature=0
    )

    prompt = f"""You are an expert Supervisor Agent directing a multi-agent AI system.
Analyze the user request and determine which specialist agent is best suited to handle it.

Available Agents:
1. 'retriever' - Use for questions about internal documentation, system info, or uploaded files.
2. 'data' - Use when relational database queries or SQL calculations are needed.
3. 'code' - Use for complex mathematical calculations, python execution, or formulas.
4. 'web' - Use for recent internet news, general world knowledge outside local docs.
5. 'direct' - Simple greetings or standard conversational chatter.

Return ONLY one word: 'retriever', 'data', 'code', 'web', or 'direct'.

User Request: {question}
"""

    response = llm.invoke(prompt).content.strip().lower()
    
    valid_routes = ["retriever", "data", "code", "web", "direct"]
    next_agent = response if response in valid_routes else "retriever"

    print(f"🎯 Supervisor qarori: '{next_agent}' yo'nalishi tanlandi.")
    
    current_steps = state.get("steps", [])
    current_steps.append(f"supervisor -> {next_agent}")

    return {
        "next_step": next_agent,
        "steps": current_steps,
        "messages": [f"Supervisor question '{question}'ni -> {next_agent} agentiga yo'naltirdi."]
    }

if __name__ == "__main__":
    test_state = {
        "question": "750000 daromaddan 350000 xarajatni ayirib foizini top",
        "documents": [],
        "revisions": 0,
        "steps": []
    }
    supervisor_node(test_state)