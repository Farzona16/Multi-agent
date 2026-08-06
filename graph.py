from langgraph.graph import StateGraph, END
from state import AgentState

# Agentlarni import qilamiz
from agents.supervisor import supervisor_node
from agents.retriever import retrieve_docs
from agents.web import search_web
from agents.data import query_sql
from agents.code import execute_python_code
from agents.critic import critic_node

# Agent Node funksiyalari
def retriever_node(state: AgentState) -> dict:
    docs = retrieve_docs(state["question"])
    context = "\n".join(docs)
    return {"documents": docs, "answer": f"Hujjatlardan topilgan ma'lumot:\n{context}"}

def web_node(state: AgentState) -> dict:
    results = search_web(state["question"])
    context = "\n".join(results)
    return {"documents": results, "answer": f"Internetdan topilgan ma'lumot:\n{context}"}

def data_node(state: AgentState) -> dict:
    res = query_sql(state["question"])
    return {"sql_result": res, "answer": res}

def code_node(state: AgentState) -> dict:
    res = execute_python_code(state["question"])
    return {"code_result": res, "answer": f"Hisob-kitob natijasi: {res}"}

def direct_node(state: AgentState) -> dict:
    return {"answer": "Salom! Men sizga ma'lumotlar tahlili va hisob-kitoblar bo'yicha yordam bera oladigan Multi-Agent tizimman. Qanday yordam bera olaman?"}

# LangGraph'ni qurish
workflow = StateGraph(AgentState)

# 1. Tugunlarni (Nodes) qo'shamiz
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("web", web_node)
workflow.add_node("data", data_node)
workflow.add_node("code", code_node)
workflow.add_node("direct", direct_node)
workflow.add_node("critic", critic_node)

# 2. Kirish nuqtasi
workflow.set_entry_point("supervisor")

# 3. Supervisor yo'naltirishi (Conditional Edges)
workflow.add_conditional_edges(
    "supervisor",
    lambda state: state["next_step"],
    {
        "retriever": "retriever",
        "web": "web",
        "data": "data",
        "code": "code",
        "direct": "direct"
    }
)

# 4. Agentlardan keyin Critic node'ga o'tish
workflow.add_edge("retriever", "critic")
workflow.add_edge("web", "critic")
workflow.add_edge("data", "critic")
workflow.add_edge("code", "critic")
workflow.add_edge("direct", END)

# 5. Critic qaroriga ko'ra tugatish yoki qayta yuborish
workflow.add_conditional_edges(
    "critic",
    lambda state: state["next_step"],
    {
        "end": END,
        "supervisor": "supervisor"
    }
)

app = workflow.compile()