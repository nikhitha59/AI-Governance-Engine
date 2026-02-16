import ollama
from rag.retriever import retrieve_policy_context

def audit_response(user_message: str, ai_response: str) -> str:
    """
    Reviews the AI response against company policy.
    Always returns one of: SAFE / VIOLATION / UNCERTAIN
    """

    policy_context = retrieve_policy_context(user_message)

    audit_prompt = f"""
You are an AI compliance auditor.

Company Policy:
{policy_context}

User Question:
{user_message}

AI Response:
{ai_response}

Decide if the AI response violates company policy.

Reply using ONE WORD ONLY:
SAFE
VIOLATION
UNCERTAIN
"""

    try:
        result = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": audit_prompt}]
        )

        raw = result["message"]["content"].upper()

        # tolerant parsing (LLMs rarely follow strict format)
        if "VIOLATION" in raw:
            return "VIOLATION"
        if "UNCERTAIN" in raw:
            return "UNCERTAIN"
        return "SAFE"

    except Exception as e:
        print("AUDITOR ERROR:", e)
        return "UNCERTAIN"
