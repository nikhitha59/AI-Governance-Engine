from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()


def mask_pii(text: str):
    """Detect and anonymize sensitive data"""

    results = analyzer.analyze(text=text, language="en")

    if not results:
        return text, [], False

    entities = list(set([r.entity_type for r in results]))

    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
        operators={
            "DEFAULT": OperatorConfig("replace", {"new_value": "[REDACTED]"})
        },
    )

    return anonymized_result.text, entities, True


def inspect_input(user_message: str):
    """Security inspection contract used by main.py"""

    cleaned_text, pii_found, has_pii = mask_pii(user_message)

    return {
        "cleaned_text": cleaned_text,
        "pii_found": pii_found,
        "has_pii": has_pii
    }
