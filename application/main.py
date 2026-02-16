from fastapi import FastAPI
from application.schemas import ChatRequest, ChatResponse
from application.llm_service import generate_response
from application.database import log_interaction
from application.security import inspect_input
from agents.auditor import audit_response
from agents.risk_engine import evaluate_risk
from rag.retriever import retrieve_policy_context
from evaluation.judge import evaluate_answer


app = FastAPI()


@app.get("/")
def root():
    return {"status": "AI Governance Engine Running (Local Model)"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Step 1 — Security inspection
    security_result = inspect_input(request.message)
    safe_message = security_result["cleaned_text"]

    # Step 2 — Retrieve policy (RAG)
    context = retrieve_policy_context(safe_message)

    # Step 3 — Executor AI
    ai_reply = generate_response(safe_message, context)

    # Step 4 — Auditor
    verdict = audit_response(safe_message, ai_reply)

    # Step 5 — Risk evaluation
    risk = evaluate_risk(verdict)

    if risk["action"] == "BLOCK":
        final_reply = "Blocked by compliance policy. (HIGH RISK)"

    elif risk["action"] == "ESCALATE":
        final_reply = f"⚠️ Potential policy concern detected.\n\n{ai_reply}"

    else:
        final_reply = ai_reply or "No response generated."

    
    #Evaluation level
    evaluation = evaluate_answer(safe_message, final_reply, context)
    print("SAFETY SCORE:", evaluation)


    # Step 6 — Logging
    log_interaction(request.message, final_reply)

    return ChatResponse(reply=final_reply)
