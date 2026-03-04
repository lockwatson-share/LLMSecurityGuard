# sanitizer/output_sanitizer.py
import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Regex patterns for sensitive info
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
PHONE_PATTERN = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
CREDIT_CARD_PATTERN = re.compile(r"\b(?:\d[ -]*?){13,16}\b", re.VERBOSE)

def sanitize_output(output: str) -> str:
    """
    Redacts sensitive info from LLM output:
    emails, SSNs, phone numbers, credit cards, and named entities.
    """
    # Regex-based redaction
    output = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", output)
    output = SSN_PATTERN.sub("[REDACTED_SSN]", output)
    output = PHONE_PATTERN.sub("[REDACTED_PHONE]", output)
    output = CREDIT_CARD_PATTERN.sub("[REDACTED_CREDIT_CARD]", output)

    # NLP-based named entity redaction (PERSON, ORG, GPE)
    doc = nlp(output)
    redacted_output = output
    # Replace sensitive entities with tags
    for ent in reversed(doc.ents):  # reverse to avoid messing up indices
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            start, end = ent.start_char, ent.end_char
            redacted_output = redacted_output[:start] + f"[REDACTED_{ent.label_}]" + redacted_output[end:]

    return redacted_output