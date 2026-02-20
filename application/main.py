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


@app .get("/")
def root():
    return {"status": "AI Governance Engine Running (Local Model)"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Step 1 — Security filter
    security_result = inspect_input(request.message)
    safe_message = security_result["cleaned_text"]

    # Step 2 — Retrieve policy
    context = retrieve_policy_context(safe_message)

    # Step 3 — Generate answer
    ai_reply = generate_response(safe_message, context)

    # Step 4 — Audit response
    audit = audit_response(safe_message, ai_reply, context)

    # Step 5 — Risk decision
    risk = evaluate_risk(audit)

    if risk["action"] == "BLOCK":
        final_reply = "Blocked by compliance policy (HIGH RISK)."

    elif risk["action"] == "ALLOW_WITH_WARNING":
        final_reply = (
            ai_reply +
            "\n\n⚠️ Note: This answer is inferred from policy context but not explicitly stated."
        )

    else:
        final_reply = ai_reply

    print("SAFETY:", risk["level"], "-", audit["reason"])

    log_interaction(request.message, final_reply)

    return ChatResponse(reply=final_reply)