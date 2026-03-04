import re
import spacy

nlp = spacy.load("en_core_web_sm")

# PII regex patterns
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
SSN_REGEX = r"\b\d{3}-\d{2}-\d{4}\b"
PHONE_REGEX = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
API_KEY_REGEX = r"\b[A-Za-z0-9]{32,}\b"  # Simple generic API key pattern

def sanitize_output(output: str) -> str:
    # Stage 1: Regex redaction
    output = re.sub(EMAIL_REGEX, "[REDACTED_EMAIL]", output)
    output = re.sub(SSN_REGEX, "[REDACTED_SSN]", output)
    output = re.sub(PHONE_REGEX, "[REDACTED_PHONE]", output)
    output = re.sub(API_KEY_REGEX, "[REDACTED_API_KEY]", output)

    # Stage 2: NLP-based NER redaction
    doc = nlp(output)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC", "MONEY", "DATE"]:
            output = output.replace(ent.text, f"[REDACTED_{ent.label_}]")

    return output