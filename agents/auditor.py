# agents/auditor.py

from application.llm_service import generate_response


def audit_response(user_query: str, ai_response: str, policy_context: str):
    """
    Determines if AI response is supported by company policy
    instead of checking exact wording.
    """

    audit_prompt = f"""
You are a corporate AI compliance auditor.

Your job is NOT to check wording similarity.
Your job is to verify whether the assistant's response is CONSISTENT with policy meaning.

POLICY:
{policy_context}

USER QUESTION:
{user_query}

ASSISTANT RESPONSE:
{ai_response}

Classify into ONE category:

SAFE:
Response meaning is supported by policy.

UNSUPPORTED:
Response adds assumptions not present in policy but not dangerous.

VIOLATION:
Response contradicts policy OR exposes restricted/sensitive handling.

Return JSON:
{{
    "verdict": "SAFE | UNSUPPORTED | VIOLATION",
    "reason": "short explanation"
}}
"""

    result = generate_response(audit_prompt,"")

    try:
        import json
        parsed = json.loads(result)
        return parsed
    except:
        return {
            "verdict": "UNSUPPORTED",
            "reason": "Auditor could not parse response"
        }