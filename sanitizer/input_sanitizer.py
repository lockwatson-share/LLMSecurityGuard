# sanitizer/input_sanitizer.py
import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Keywords and sensitive patterns
DANGEROUS_KEYWORDS = ["delete", "drop", "shutdown", "rm -rf", "exfiltrate", "format"]
SENSITIVE_ENTITIES = ["PASSWORD", "SSN", "CREDIT_CARD", "EMAIL", "PHONE"]

# Regex patterns for sensitive info
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
PHONE_PATTERN = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
CREDIT_CARD_PATTERN = re.compile(r"\b(?:\d[ -]*?){13,16}\b", re.VERBOSE)
PASSWORD_KEYWORDS = ["password", "secret", "passwd", "token", "apikey"]

def calculate_risk(prompt: str, user: str = "") -> int:
    """
    Returns risk score based on dangerous keywords and sensitive info.
    """
    score = 0
    prompt_lower = prompt.lower()

    # Dangerous commands
    for word in DANGEROUS_KEYWORDS:
        if word in prompt_lower:
            score += 50

    # Sensitive keywords
    for word in PASSWORD_KEYWORDS:
        if word in prompt_lower:
            score += 30

    # Regex-based sensitive info
    if EMAIL_PATTERN.search(prompt):
        score += 20
    if SSN_PATTERN.search(prompt):
        score += 30
    if PHONE_PATTERN.search(prompt):
        score += 20
    if CREDIT_CARD_PATTERN.search(prompt):
        score += 30

    # Use NLP to detect named entities (e.g., PERSON, ORG, GPE)
    doc = nlp(prompt)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            score += 10

    return min(score, 100)

def sanitize_input(prompt: str, user: str = ""):
    """
    Returns sanitized prompt and risk score.
    Currently, sanitization is minimal; in future, could redact sensitive info.
    """
    risk_score = calculate_risk(prompt, user)
    sanitized_prompt = prompt  # Placeholder; could add redaction here
    return sanitized_prompt, risk_score