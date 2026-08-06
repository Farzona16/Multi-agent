from typing import TypedDict, List, Optional, Annotated
import operator

class AgentState(TypedDict):
    question: str               # Foydalanuvchining asl savoli
    plan: Optional[str]         # Supervisor tuzgan reja
    next_step: Optional[str]    # Keyingi qaysi agentga o'tishi (routing)
    documents: List[str]        # Vektor baza yoki Web search'dan topilgan hujjatlar
    sql_result: Optional[str]   # Data agent bajarib kelgan SQL natijasi
    code_result: Optional[str]  # Code agent bajargan Python natijasi
    answer: Optional[str]       # Yakuniy shakllantirilgan javob
    steps: List[str]            # Qaysi agentlar ishlatilgani tarixi
    revisions: int              # Critic rad etib, qayta ko'rishlar soni
    messages: Annotated[List[str], operator.add]  # LangGraph reducer loglari