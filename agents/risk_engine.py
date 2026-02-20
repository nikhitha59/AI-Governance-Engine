# agents/risk_engine.py

def evaluate_risk(audit_result: dict):
    """
    Converts audit verdict into governance action
    """

    verdict = audit_result.get("verdict", "UNSUPPORTED")

    if verdict == "VIOLATION":
        return {
            "level": "HIGH",
            "action": "BLOCK"
        }

    elif verdict == "UNSUPPORTED":
        return {
            "level": "MEDIUM",
            "action": "ALLOW_WITH_WARNING"
        }

    else:
        return {
            "level": "LOW",
            "action": "ALLOW"
        }