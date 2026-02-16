import ollama


def generate_response(user_message: str, context: str = ""):
    """
    Generate LLM response using company policy context
    """

    system_prompt = f"""
You are a company compliance assistant.
Answer the user's question using the provided company policy.

Company Policy:
{context}

Rules:
-Never acknowledge receiving personal data
- Never mention SSN, credit card, phone number, or any private identifier
- If sensitive info was detected, behave as if it never existed
- Answer only using company policy context
- Be concise and professional
- Follow the policy strictly
- Do not invent policies
- If policy does not cover it, say policy does not specify
- Only explain company policy
- Do NOT suggest contacting supervisors, HR, legal teams, or support staff
- Do NOT recommend escalation
- Do NOT add conversational closing statements
- Do NOT provide advice outside policy
- If policy forbids something, simply state it is not allowed
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )

        return response["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", str(e))
        return "AI service temporarily unavailable."
