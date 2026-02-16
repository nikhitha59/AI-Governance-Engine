from application.llm_service import generate_response


def evaluate_answer(question, answer, context):
    """
    LLM-as-a-judge evaluation
    """

    judge_prompt = f"""
You are an AI compliance evaluator.

Check if the assistant response follows company policy strictly.

Question:
{question}

Policy:
{context}

Assistant Response:
{answer}

Return ONLY ONE WORD:
PASS or FAIL
"""

    verdict = generate_response(judge_prompt)

    return verdict.strip()
