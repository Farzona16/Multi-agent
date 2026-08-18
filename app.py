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
#     demo.launch()

# import os
# import gradio as gr
# from dotenv import load_dotenv
# from graph import app as agent_graph
# from memory import save_turn_to_memory, get_relevant_history

# load_dotenv()

# def get_langfuse_handler():
#     try:
#         from langfuse.langchain import CallbackHandler
#         return CallbackHandler(
#             public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
#             secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
#             host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
#         )
#     except Exception:
#         return None

# def predict(message, history):
#     if not message or not message.strip():
#         return ""
    
#     # 1. Memory'dan suhbat tarixini olish
#     past_history = get_relevant_history(message)
    
#     # 2. Agent state tayyorlash
#     initial_state = {
#         "question": message,
#         "documents": [],
#         "revisions": 0,
#         "steps": [],
#         "messages": []
#     }
    
#     # 3. Callback
#     handler = get_langfuse_handler()
#     config = {"callbacks": [handler]} if handler else {}
    
#     # 4. Graph yuritish
#     res = agent_graph.invoke(initial_state, config=config)
#     answer = res.get("answer", "Javob shakllantirilmadi.")
    
#     # 5. Memory'ga saqlash
#     save_turn_to_memory(message, answer)
    
#     return answer

# # Zamonaviy Soft/Ocean mavzusini va Custom CSS ni qo'llash
# custom_css = """
# #main-header {
#     text-align: center;
#     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     color: white;
#     padding: 20px;
#     border-radius: 12px;
#     margin-bottom: 20px;
# }
# #main-header h1 {
#     font-size: 2.2em;
#     font-weight: 700;
#     margin-bottom: 5px;
# }
# #main-header p {
#     font-size: 1.1em;
#     opacity: 0.9;
# }
# """

# with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="slate"), css=custom_css) as demo:
#     gr.HTML(
#         """
#         <div id="main-header">
#             <h1>🚀 Multi-Agent AI Analyst System</h1>
#             <p>LangGraph, Gemini, Qdrant & Tavily bilan ta'minlangan avtonom sun'iy intelekt tizimi</p>
#         </div>
#         """
#     )
    
#     gr.ChatInterface(
#         fn=predict,
#         textbox=gr.Textbox(placeholder="Savolingizni yoki analitik topshiriqni kiriting...", container=False, scale=7),
#         examples=[
#             "Python orqali 15 ning kvadratini hisoblang",
#             "Kompaniyaning umumiy daromadi qancha?",
#             "Oxirgi sun'iy intelekt yangiliklarini topib ber"
#         ],
#         cache_examples=False
#     )

# if __name__ == "__main__":
#     demo.launch()

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
#         return CallbackHandler(
#             public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
#             secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
#             host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
#         )
#     except Exception:
#         try:
#             from langfuse.callback import CallbackHandler
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


# # --- PROFESSIONAL SAAS UI CUSTOM STYLES (CSS) ---
# custom_css = """
# /* Google Font yuklash */
# @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

# :root, .dark, .gradio-container {
#     color-scheme: light !important;

#     /* --- Gradio o'zgaruvchilarini majburan qayta belgilaymiz (dark mode'ni yengish uchun) --- */
#     --body-background-fill: #f5f6fb !important;
#     --background-fill-primary: #ffffff !important;
#     --background-fill-secondary: #f8fafc !important;
#     --block-background-fill: #ffffff !important;
#     --block-border-color: #e2e8f0 !important;
#     --block-label-background-fill: #ffffff !important;
#     --block-label-text-color: #475569 !important;
#     --border-color-primary: #e2e8f0 !important;
#     --border-color-accent: #6366f1 !important;
#     --input-background-fill: #ffffff !important;
#     --input-border-color: #cbd5e1 !important;
#     --body-text-color: #0f172a !important;
#     --body-text-color-subdued: #64748b !important;
#     --color-accent: #6366f1 !important;
#     --color-accent-soft: #eef2ff !important;
#     --link-text-color: #4f46e5 !important;
#     --button-primary-background-fill: #4f46e5 !important;
#     --button-primary-background-fill-hover: #4338ca !important;
#     --button-primary-text-color: #ffffff !important;
#     --button-secondary-background-fill: #ffffff !important;
#     --button-secondary-border-color: #cbd5e1 !important;
#     --button-secondary-text-color: #475569 !important;
#     --chatbot-text-size: 14.5px !important;

#     --brand-50: #eef2ff;
#     --brand-100: #e0e7ff;
#     --brand-400: #818cf8;
#     --brand-500: #6366f1;
#     --brand-600: #4f46e5;
#     --brand-700: #4338ca;
#     --ink-900: #0f172a;
#     --ink-600: #475569;
#     --ink-400: #94a3b8;
#     --line: #e2e8f0;
# }

# * {
#     font-family: 'Plus Jakarta Sans', sans-serif !important;
# }

# /* Sahifaning butun foni (konteynerdan tashqari qismi ham) */
# html, body {
#     background: #f5f6fb !important;
# }

# body, .gradio-container, .gradio-container.dark, gradio-app {
#     background: #f5f6fb !important;
#     background-image:
#         radial-gradient(circle at 15% 10%, rgba(99, 102, 241, 0.10) 0%, transparent 45%),
#         radial-gradient(circle at 85% 0%, rgba(129, 140, 248, 0.10) 0%, transparent 40%),
#         radial-gradient(#e2e8f0 1px, transparent 1px) !important;
#     background-size: auto, auto, 22px 22px !important;
# }

# /* Konteyner */
# .gradio-container {
#     max-width: 900px !important;
#     width: 100% !important;
#     margin: 0 auto !important;
#     padding: 2.5rem 1.25rem !important;
#     box-sizing: border-box !important;
# }

# /* Har qanday ichki blok (chatbot, textbox o'ramlari) fonini oq qilamiz */
# .block, .form, .panel, .contain {
#     background: transparent !important;
#     border-color: var(--line) !important;
# }

# /* Header UI */
# .header-card {
#     position: relative;
#     background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
#     padding: 30px 24px !important;
#     border-radius: 22px !important;
#     border: 1px solid var(--line) !important;
#     box-shadow: 0 10px 30px -8px rgba(79, 70, 229, 0.15), 0 2px 8px rgba(15, 23, 42, 0.04) !important;
#     margin-bottom: 22px !important;
#     text-align: center;
#     overflow: hidden;
# }

# .header-card::before {
#     content: "";
#     position: absolute;
#     top: -60%;
#     left: 50%;
#     transform: translateX(-50%);
#     width: 420px;
#     height: 200px;
#     background: radial-gradient(ellipse at center, rgba(99, 102, 241, 0.22) 0%, transparent 70%);
#     pointer-events: none;
# }

# .header-card h1 {
#     color: var(--ink-900) !important;
#     font-size: 27px !important;
#     font-weight: 800 !important;
#     margin-bottom: 6px !important;
#     letter-spacing: -0.02em;
# }

# .header-card p {
#     color: var(--ink-600) !important;
#     font-size: 14px !important;
#     margin: 0 !important;
#     font-weight: 500;
# }

# .header-badges {
#     display: flex;
#     justify-content: center;
#     gap: 8px;
#     flex-wrap: wrap;
#     margin-top: 14px;
# }

# .header-badge {
#     display: inline-flex;
#     align-items: center;
#     gap: 6px;
#     background: var(--brand-50);
#     color: var(--brand-700);
#     border: 1px solid var(--brand-100);
#     padding: 5px 12px;
#     border-radius: 999px;
#     font-size: 12px;
#     font-weight: 600;
#     white-space: nowrap;
# }

# /* Chatbot Oynasi */
# #app-chatbot {
#     background: #ffffff !important;
#     border: 1px solid var(--line) !important;
#     border-radius: 20px !important;
#     box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.06) !important;
#     padding: 14px !important;
# }

# #app-chatbot .bubble-wrap {
#     background: transparent !important;
# }

# /* Message Bubble'lar (Foydalanuvchi va Agent) */
# #app-chatbot .message.user {
#     background: linear-gradient(135deg, var(--brand-500) 0%, var(--brand-700) 100%) !important;
#     color: #ffffff !important;
#     border: none !important;
#     border-radius: 18px 18px 4px 18px !important;
#     font-size: 14.5px !important;
#     line-height: 1.55 !important;
#     padding: 13px 18px !important;
#     box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25) !important;
# }

# #app-chatbot .message.user * {
#     color: #ffffff !important;
# }

# #app-chatbot .message.bot {
#     background: #f8fafc !important;
#     color: var(--ink-900) !important;
#     border: 1px solid var(--line) !important;
#     border-radius: 18px 18px 18px 4px !important;
#     font-size: 14.5px !important;
#     line-height: 1.55 !important;
#     padding: 13px 18px !important;
# }

# #app-chatbot .message.bot * {
#     color: var(--ink-900) !important;
# }

# /* Nusxa olish/qayta yuborish kabi mayda tugmalar */
# #app-chatbot button {
#     background: #ffffff !important;
#     border: 1px solid var(--line) !important;
#     color: var(--ink-600) !important;
#     border-radius: 8px !important;
#     box-shadow: 0 2px 6px rgba(15, 23, 42, 0.06) !important;
# }

# #app-chatbot button:hover {
#     color: var(--brand-700) !important;
#     border-color: var(--brand-400) !important;
# }

# /* Input (Matn kiritish) maydoni */
# #app-textbox textarea, #app-textbox input[type="text"] {
#     background: #ffffff !important;
#     border: 1.5px solid #cbd5e1 !important;
#     border-radius: 14px !important;
#     color: var(--ink-900) !important;
#     font-size: 14.5px !important;
#     padding: 14px 16px !important;
#     transition: all 0.2s ease !important;
# }

# #app-textbox textarea:focus, #app-textbox input[type="text"]:focus {
#     border-color: var(--brand-500) !important;
#     box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.14) !important;
#     outline: none !important;
# }

# #app-textbox textarea::placeholder, #app-textbox input[type="text"]::placeholder {
#     color: var(--ink-400) !important;
# }

# /* Yuborish tugmasi */
# button.primary {
#     background: linear-gradient(135deg, var(--brand-500) 0%, var(--brand-700) 100%) !important;
#     color: #ffffff !important;
#     font-weight: 600 !important;
#     font-size: 14px !important;
#     border-radius: 14px !important;
#     border: none !important;
#     padding: 12px 26px !important;
#     box-shadow: 0 6px 16px rgba(79, 70, 229, 0.28) !important;
#     transition: all 0.2s ease !important;
# }

# button.primary:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 20px rgba(79, 70, 229, 0.38) !important;
# }

# button.primary:active {
#     transform: translateY(0) !important;
# }

# /* Tugmalarning ikkilamchi variantlari (Clear, Retry va hk) */
# button.secondary {
#     background: #ffffff !important;
#     color: var(--ink-600) !important;
#     border: 1.5px solid #cbd5e1 !important;
#     border-radius: 14px !important;
#     font-weight: 500 !important;
#     transition: all 0.2s ease !important;
# }

# button.secondary:hover {
#     background: var(--brand-50) !important;
#     color: var(--brand-700) !important;
#     border-color: var(--brand-400) !important;
# }

# /* Scrollbar */
# ::-webkit-scrollbar {
#     width: 8px;
#     height: 8px;
# }
# ::-webkit-scrollbar-track {
#     background: transparent;
# }
# ::-webkit-scrollbar-thumb {
#     background: #cbd5e1;
#     border-radius: 8px;
# }
# ::-webkit-scrollbar-thumb:hover {
#     background: var(--brand-400);
# }

# /* Footer */
# .footer-note {
#     text-align: center;
#     color: var(--ink-400) !important;
#     font-size: 12px !important;
#     margin-top: 18px !important;
# }

# /* ================= RESPONSIVE (mobil / planshet) ================= */
# @media (max-width: 768px) {
#     .gradio-container {
#         padding: 1.25rem 0.75rem !important;
#     }
#     .header-card {
#         padding: 22px 16px !important;
#         border-radius: 18px !important;
#     }
#     .header-card h1 {
#         font-size: 21px !important;
#     }
#     .header-card p {
#         font-size: 12.5px !important;
#     }
#     .header-badge {
#         font-size: 11px !important;
#         padding: 4px 10px !important;
#     }
#     #app-chatbot {
#         border-radius: 16px !important;
#         padding: 8px !important;
#     }
#     #app-chatbot .message.user, #app-chatbot .message.bot {
#         font-size: 13.5px !important;
#         padding: 10px 14px !important;
#     }
#     #app-textbox textarea, #app-textbox input[type="text"] {
#         font-size: 13.5px !important;
#         padding: 12px 14px !important;
#     }
#     button.primary, button.secondary {
#         padding: 10px 16px !important;
#         font-size: 13px !important;
#     }
# }

# @media (max-width: 480px) {
#     .header-card h1 {
#         font-size: 18px !important;
#     }
#     .header-badges {
#         gap: 6px !important;
#     }
#     .header-badge {
#         font-size: 10.5px !important;
#     }
# }
# """

# force_light_mode_js = """
# function() {
#     document.body.classList.remove('dark');
#     document.body.classList.add('light');
#     document.documentElement.classList.remove('dark');
#     document.documentElement.classList.add('light');
#     const app = document.querySelector('gradio-app');
#     if (app) {
#         app.classList.remove('dark');
#         app.classList.add('light');
#     }
#     const container = document.querySelector('.gradio-container');
#     if (container) {
#         container.classList.remove('dark');
#         container.classList.add('light');
#     }
# }
# """

# theme = gr.themes.Soft(
#     primary_hue="indigo",
#     secondary_hue="slate",
#     neutral_hue="slate"
# )

# # --- APPLICATION UI ---
# with gr.Blocks(title="Multi-Agent AI Analyst System") as demo:

#     # Custom Header Block
#     with gr.Column(elem_classes="header-card"):
#         gr.Markdown(
#             """
#             # 🚀 Multi-Agent AI Analyst System
#             LangGraph, Gemini, Qdrant, Langfuse va Tavily bilan quvvatlangan avtonom tahliliy tizim
#             """
#         )
#         gr.HTML(
#             """
#             <div class="header-badges">
#                 <span class="header-badge">⚡ LangGraph</span>
#                 <span class="header-badge">🧠 Gemini</span>
#                 <span class="header-badge">📚 Qdrant</span>
#                 <span class="header-badge">🔍 Langfuse</span>
#                 <span class="header-badge">🌐 Tavily</span>
#             </div>
#             """
#         )

#     # Chat Interface
#     gr.ChatInterface(
#         fn=chat_interface,
#         chatbot=gr.Chatbot(
#             elem_id="app-chatbot",
#             height=480,
#             avatar_images=None,
#             show_label=False
#         ),
#         textbox=gr.Textbox(
#             elem_id="app-textbox",
#             placeholder="Savolingizni yoki tahlil uchun topshiriqni kiriting...",
#             container=False,
#             scale=7
#         )
#     )

#     gr.HTML('<div class="footer-note">Multi-Agent AI Analyst · Powered by Farzonaxon\'s Capstone Project</div>')

# if __name__ == "__main__":
#     # Render muhitida RENDER=true o'zgaruvchisi avtomatik bo'ladi yoki PORT beriladi
#     is_render = os.environ.get("RENDER") or os.environ.get("PORT")
    
#     server_name = "0.0.0.0"
#     port = int(os.environ.get("PORT", 7860))
    
#     demo.launch(
#         server_name=server_name,
#         server_port=port,
#         theme=theme,
#         css=custom_css,
#         js=force_light_mode_js
#     )

import os
import gradio as gr
from dotenv import load_dotenv
from graph import app as agent_graph
from memory import save_turn_to_memory, get_relevant_history

load_dotenv()

# Langfuse Handler'ni versiyaga mos ravishda xavfsiz init qilish
def get_langfuse_handler():
    try:
        from langfuse.langchain import CallbackHandler
        return CallbackHandler(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        )
    except Exception:
        try:
            from langfuse.callback import CallbackHandler
            return CallbackHandler()
        except Exception:
            return None

def chat_interface(user_message, history):
    if not user_message or user_message.strip() == "":
        return ""
    
    # 1. Memory'dan tegishli suhbat tarixini olamiz
    past_history = get_relevant_history(user_message)
    
    # 2. LangGraph boshlang'ich holati (suhbat tarixi context sifatida uzatiladi)
    initial_state = {
        "question": user_message,
        "documents": [],
        "revisions": 0,
        "steps": [],
        "messages": [("system", f"O'tgan suhbatlar konteksti: {past_history}")] if past_history else []
    }
    
    # 3. Langfuse callback tayyorlash
    handler = get_langfuse_handler()
    config = {}
    if handler:
        config["callbacks"] = [handler]
    
    # 4. Agentlar zanjirini yurgizish
    res = agent_graph.invoke(initial_state, config=config)
    answer = res.get("answer", "Javob shakllantirilmadi.")
    
    # 5. Natijani Memory'ga saqlash
    save_turn_to_memory(user_message, answer)
    
    return answer


# --- PROFESSIONAL SAAS UI CUSTOM STYLES (CSS) ---
custom_css = """
/* Google Font yuklash */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root, .dark, .gradio-container {
    color-scheme: light !important;

    /* --- Gradio o'zgaruvchilarini majburan qayta belgilaymiz (dark mode'ni yengish uchun) --- */
    --body-background-fill: #f5f6fb !important;
    --background-fill-primary: #ffffff !important;
    --background-fill-secondary: #f8fafc !important;
    --block-background-fill: #ffffff !important;
    --block-border-color: #e2e8f0 !important;
    --block-label-background-fill: #ffffff !important;
    --block-label-text-color: #475569 !important;
    --border-color-primary: #e2e8f0 !important;
    --border-color-accent: #6366f1 !important;
    --input-background-fill: #ffffff !important;
    --input-border-color: #cbd5e1 !important;
    --body-text-color: #0f172a !important;
    --body-text-color-subdued: #64748b !important;
    --color-accent: #6366f1 !important;
    --color-accent-soft: #eef2ff !important;
    --link-text-color: #4f46e5 !important;
    --button-primary-background-fill: #4f46e5 !important;
    --button-primary-background-fill-hover: #4338ca !important;
    --button-primary-text-color: #ffffff !important;
    --button-secondary-background-fill: #ffffff !important;
    --button-secondary-border-color: #cbd5e1 !important;
    --button-secondary-text-color: #475569 !important;
    --chatbot-text-size: 14.5px !important;

    --brand-50: #eef2ff;
    --brand-100: #e0e7ff;
    --brand-400: #818cf8;
    --brand-500: #6366f1;
    --brand-600: #4f46e5;
    --brand-700: #4338ca;
    --ink-900: #0f172a;
    --ink-600: #475569;
    --ink-400: #94a3b8;
    --line: #e2e8f0;
}

* {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* Sahifaning butun foni (konteynerdan tashqari qismi ham) */
html, body {
    background: #f5f6fb !important;
}

body, .gradio-container, .gradio-container.dark, gradio-app {
    background: #f5f6fb !important;
    background-image:
        radial-gradient(circle at 15% 10%, rgba(99, 102, 241, 0.10) 0%, transparent 45%),
        radial-gradient(circle at 85% 0%, rgba(129, 140, 248, 0.10) 0%, transparent 40%),
        radial-gradient(#e2e8f0 1px, transparent 1px) !important;
    background-size: auto, auto, 22px 22px !important;
}

/* Konteyner */
.gradio-container {
    max-width: 900px !important;
    width: 100% !important;
    margin: 0 auto !important;
    padding: 2.5rem 1.25rem !important;
    box-sizing: border-box !important;
}

/* Har qanday ichki blok (chatbot, textbox o'ramlari) fonini oq qilamiz */
.block, .form, .panel, .contain {
    background: transparent !important;
    border-color: var(--line) !important;
}

/* Header UI */
.header-card {
    position: relative;
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    padding: 30px 24px !important;
    border-radius: 22px !important;
    border: 1px solid var(--line) !important;
    box-shadow: 0 10px 30px -8px rgba(79, 70, 229, 0.15), 0 2px 8px rgba(15, 23, 42, 0.04) !important;
    margin-bottom: 22px !important;
    text-align: center;
    overflow: hidden;
}

.header-card::before {
    content: "";
    position: absolute;
    top: -60%;
    left: 50%;
    transform: translateX(-50%);
    width: 420px;
    height: 200px;
    background: radial-gradient(ellipse at center, rgba(99, 102, 241, 0.22) 0%, transparent 70%);
    pointer-events: none;
}

.header-card h1 {
    color: var(--ink-900) !important;
    font-size: 27px !important;
    font-weight: 800 !important;
    margin-bottom: 6px !important;
    letter-spacing: -0.02em;
}

.header-card p {
    color: var(--ink-600) !important;
    font-size: 14px !important;
    margin: 0 !important;
    font-weight: 500;
}

.header-badges {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 14px;
}

.header-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--brand-50);
    color: var(--brand-700);
    border: 1px solid var(--brand-100);
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
}

/* Chatbot Oynasi */
#app-chatbot {
    background: #ffffff !important;
    border: 1px solid var(--line) !important;
    border-radius: 20px !important;
    box-shadow: 0 12px 28px -6px rgba(15, 23, 42, 0.06) !important;
    padding: 14px !important;
}

#app-chatbot .bubble-wrap {
    background: transparent !important;
}

/* Message Bubble'lar (Foydalanuvchi va Agent) */
#app-chatbot .message.user {
    background: linear-gradient(135deg, var(--brand-500) 0%, var(--brand-700) 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 18px 18px 4px 18px !important;
    font-size: 14.5px !important;
    line-height: 1.55 !important;
    padding: 13px 18px !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25) !important;
}

#app-chatbot .message.user * {
    color: #ffffff !important;
}

#app-chatbot .message.bot {
    background: #f8fafc !important;
    color: var(--ink-900) !important;
    border: 1px solid var(--line) !important;
    border-radius: 18px 18px 18px 4px !important;
    font-size: 14.5px !important;
    line-height: 1.55 !important;
    padding: 13px 18px !important;
}

#app-chatbot .message.bot * {
    color: var(--ink-900) !important;
}

/* Nusxa olish/qayta yuborish kabi mayda tugmalar */
#app-chatbot button {
    background: #ffffff !important;
    border: 1px solid var(--line) !important;
    color: var(--ink-600) !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 6px rgba(15, 23, 42, 0.06) !important;
}

#app-chatbot button:hover {
    color: var(--brand-700) !important;
    border-color: var(--brand-400) !important;
}

/* Input (Matn kiritish) maydoni */
#app-textbox textarea, #app-textbox input[type="text"] {
    background: #ffffff !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 14px !important;
    color: var(--ink-900) !important;
    font-size: 14.5px !important;
    padding: 14px 16px !important;
    transition: all 0.2s ease !important;
}

#app-textbox textarea:focus, #app-textbox input[type="text"]:focus {
    border-color: var(--brand-500) !important;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.14) !important;
    outline: none !important;
}

#app-textbox textarea::placeholder, #app-textbox input[type="text"]::placeholder {
    color: var(--ink-400) !important;
}

/* Yuborish tugmasi */
button.primary {
    background: linear-gradient(135deg, var(--brand-500) 0%, var(--brand-700) 100%) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 12px 26px !important;
    box-shadow: 0 6px 16px rgba(79, 70, 229, 0.28) !important;
    transition: all 0.2s ease !important;
}

button.primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(79, 70, 229, 0.38) !important;
}

button.primary:active {
    transform: translateY(0) !important;
}

/* Tugmalarning ikkilamchi variantlari (Clear, Retry va hk) */
button.secondary {
    background: #ffffff !important;
    color: var(--ink-600) !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 14px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

button.secondary:hover {
    background: var(--brand-50) !important;
    color: var(--brand-700) !important;
    border-color: var(--brand-400) !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 8px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--brand-400);
}

/* Footer */
.footer-note {
    text-align: center;
    color: var(--ink-400) !important;
    font-size: 12px !important;
    margin-top: 18px !important;
}

/* ================= RESPONSIVE (mobil / planshet) ================= */
@media (max-width: 768px) {
    .gradio-container {
        padding: 1.25rem 0.75rem !important;
    }
    .header-card {
        padding: 22px 16px !important;
        border-radius: 18px !important;
    }
    .header-card h1 {
        font-size: 21px !important;
    }
    .header-card p {
        font-size: 12.5px !important;
    }
    .header-badge {
        font-size: 11px !important;
        padding: 4px 10px !important;
    }
    #app-chatbot {
        border-radius: 16px !important;
        padding: 8px !important;
    }
    #app-chatbot .message.user, #app-chatbot .message.bot {
        font-size: 13.5px !important;
        padding: 10px 14px !important;
    }
    #app-textbox textarea, #app-textbox input[type="text"] {
        font-size: 13.5px !important;
        padding: 12px 14px !important;
    }
    button.primary, button.secondary {
        padding: 10px 16px !important;
        font-size: 13px !important;
    }
}

@media (max-width: 480px) {
    .header-card h1 {
        font-size: 18px !important;
    }
    .header-badges {
        gap: 6px !important;
    }
    .header-badge {
        font-size: 10.5px !important;
    }
}
"""

force_light_mode_js = """
function() {
    document.body.classList.remove('dark');
    document.body.classList.add('light');
    document.documentElement.classList.remove('dark');
    document.documentElement.classList.add('light');
    const app = document.querySelector('gradio-app');
    if (app) {
        app.classList.remove('dark');
        app.classList.add('light');
    }
    const container = document.querySelector('.gradio-container');
    if (container) {
        container.classList.remove('dark');
        container.classList.add('light');
    }
}
"""

theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="slate",
    neutral_hue="slate"
)

# --- APPLICATION UI ---
with gr.Blocks(title="Multi-Agent AI Analyst System") as demo:

    # Custom Header Block
    with gr.Column(elem_classes="header-card"):
        gr.Markdown(
            """
            # 🚀 Multi-Agent AI Analyst System
            LangGraph, Gemini, Qdrant, Langfuse va Tavily bilan quvvatlangan avtonom tahliliy tizim
            """
        )
        gr.HTML(
            """
            <div class="header-badges">
                <span class="header-badge">⚡ LangGraph</span>
                <span class="header-badge">🧠 Gemini</span>
                <span class="header-badge">📚 Qdrant</span>
                <span class="header-badge">🔍 Langfuse</span>
                <span class="header-badge">🌐 Tavily</span>
            </div>
            """
        )

    # Chat Interface
    gr.ChatInterface(
        fn=chat_interface,
        chatbot=gr.Chatbot(
            elem_id="app-chatbot",
            height=480,
            avatar_images=None,
            show_label=False
        ),
        textbox=gr.Textbox(
            elem_id="app-textbox",
            placeholder="Savolingizni yoki tahlil uchun topshiriqni kiriting...",
            container=False,
            scale=7
        )
    )

    gr.HTML('<div class="footer-note">Multi-Agent AI Analyst · Powered by Farzonaxon\'s Capstone Project</div>')

if __name__ == "__main__":
    server_name = "0.0.0.0"
    port = int(os.environ.get("PORT", 7860))
    
    demo.launch(
        server_name=server_name,
        server_port=port,
        theme=theme,
        css=custom_css,
        js=force_light_mode_js
    )