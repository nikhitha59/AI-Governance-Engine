from application.llm_service import generate_response


# evaluation/judge.py

def evaluate_answer(question, answer, context):
    """
    Lightweight evaluation layer.
    Only checks if model actually answered something.
    No heavy NLP models.
    """
    if not answer or len(answer.strip()) < 10:
        return "FAIL"

    if "blocked by compliance" in answer.lower():
        return "BLOCKED"

    return "PASS"
