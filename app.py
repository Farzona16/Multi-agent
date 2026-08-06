# import os
# import gradio as gr
# from dotenv import load_dotenv
# from graph import app as agent_graph
# from memory import save_turn_to_memory, get_relevant_history

# load_dotenv()

# # Langfuse Handler'ni versiyaga mos ravishda xavfsiz init qilish
# def get_langfuse_handler():
#     try:
#         from langfuse.langchain import CallbackHandler
#         # Langfuse v3+ versiyalari uchun
#         return CallbackHandler(
#             public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
#             secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
#             host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
#         )
#     except Exception:
#         try:
#             from langfuse.callback import CallbackHandler
#             # Eski versiyalar muqobili
#             return CallbackHandler()
#         except Exception:
#             return None

# def chat_interface(user_message, history):
#     if not user_message or user_message.strip() == "":
#         return ""
    
#     # 1. Memory'dan tegishli suhbat tarixini olamiz
#     past_history = get_relevant_history(user_message)
    
#     # 2. LangGraph boshlang'ich holati
#     initial_state = {
#         "question": user_message,
#         "documents": [],
#         "revisions": 0,
#         "steps": [],
#         "messages": []
#     }
    
#     # 3. Langfuse callback tayyorlash
#     handler = get_langfuse_handler()
#     config = {}
#     if handler:
#         config["callbacks"] = [handler]
    
#     # 4. Agentlar zanjirini yurgizish
#     res = agent_graph.invoke(initial_state, config=config)
#     answer = res.get("answer", "Javob shakllantirilmadi.")
    
#     # 5. Natijani Memory'ga saqlash
#     save_turn_to_memory(user_message, answer)
    
#     return answer

# # Gradio ChatInterface interfeysi
# demo = gr.ChatInterface(
#     fn=chat_interface,
#     title="Multi-Agent AI Analyst System",
#     description="LangGraph, Gemini, Qdrant, Langfuse va Tavily bilan boyitilgan avtonom analitik tizim."
# )

# if __name__ == "__main__":
#     demo.launch(share=True)

import os
import gradio as gr
from dotenv import load_dotenv
from graph import app as agent_graph
from memory import save_turn_to_memory, get_relevant_history

load_dotenv()

def get_langfuse_handler():
    try:
        from langfuse.langchain import CallbackHandler
        return CallbackHandler(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        )
    except Exception:
        return None

def predict(message, history):
    if not message or not message.strip():
        return ""
    
    # 1. Memory'dan suhbat tarixini olish
    past_history = get_relevant_history(message)
    
    # 2. Agent state tayyorlash
    initial_state = {
        "question": message,
        "documents": [],
        "revisions": 0,
        "steps": [],
        "messages": []
    }
    
    # 3. Callback
    handler = get_langfuse_handler()
    config = {"callbacks": [handler]} if handler else {}
    
    # 4. Graph yuritish
    res = agent_graph.invoke(initial_state, config=config)
    answer = res.get("answer", "Javob shakllantirilmadi.")
    
    # 5. Memory'ga saqlash
    save_turn_to_memory(message, answer)
    
    return answer

# Zamonaviy Soft/Ocean mavzusini va Custom CSS ni qo'llash
custom_css = """
#main-header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
#main-header h1 {
    font-size: 2.2em;
    font-weight: 700;
    margin-bottom: 5px;
}
#main-header p {
    font-size: 1.1em;
    opacity: 0.9;
}
"""

with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="slate"), css=custom_css) as demo:
    gr.HTML(
        """
        <div id="main-header">
            <h1>🚀 Multi-Agent AI Analyst System</h1>
            <p>LangGraph, Gemini, Qdrant & Tavily bilan ta'minlangan avtonom sun'iy intelekt tizimi</p>
        </div>
        """
    )
    
    gr.ChatInterface(
        fn=predict,
        textbox=gr.Textbox(placeholder="Savolingizni yoki analitik topshiriqni kiriting...", container=False, scale=7),
        examples=[
            "Python orqali 15 ning kvadratini hisoblang",
            "Kompaniyaning umumiy daromadi qancha?",
            "Oxirgi sun'iy intelekt yangiliklarini topib ber"
        ],
        cache_examples=False
    )

if __name__ == "__main__":
    demo.launch()