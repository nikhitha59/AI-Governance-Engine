def evaluate_risk(verdict: str):

    verdict = verdict.upper().strip()

    if verdict == "SAFE":
        return {
            "risk_level": "LOW",
            "action": "ALLOW"
        }

    if verdict == "UNCERTAIN":
        return {
            "risk_level": "MEDIUM",
            "action": "ESCALATE"
        }

    if verdict == "VIOLATION":
        return {
            "risk_level": "HIGH",
            "action": "BLOCK"
        }

    return {
        "risk_level": "UNKNOWN",
        "action": "ESCALATE"
    }
