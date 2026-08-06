from graph import app

def run_query(question: str):
    print(f"\n==========================================")
    print(f"❓ Savol: {question}")
    print(f"==========================================")
    
    initial_state = {
        "question": question,
        "documents": [],
        "revisions": 0,
        "steps": [],
        "messages": []
    }
    
    # LangGraph pipeline'ni ishga tushirish
    final_output = app.invoke(initial_state)
    
    print("\n💡 **YAKUNIY JAVOB:**")
    print(final_output.get("answer"))
    print("==========================================\n")

if __name__ == "__main__":
    # Test 1: Code agent (Matematik hisob-kitob)
    run_query("750000 daromaddan 350000 xarajatni ayirib, foyda foizini toping")
    
    # Test 2: Local Vector Store (Retriever Agent)
    run_query("Multi-Agent AI Analyst loyihasida qanday agentlar bor?")