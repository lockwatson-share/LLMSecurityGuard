import re
import spacy

# Load spaCy small English model for NLP
nlp = spacy.load("en_core_web_sm")

# Keywords & sensitive info
DANGEROUS_KEYWORDS = ["delete", "drop", "shutdown", "rm -rf", "exfiltrate"]
SENSITIVE_INFO = ["password", "secret", "ssn", "credit card", "token", "api key"]

def calculate_risk(prompt: str, user: str = "") -> int:
    score = 0
    prompt_lower = prompt.lower()

    # Stage 1: Keyword scoring
    for word in DANGEROUS_KEYWORDS:
        if re.search(rf"\b{re.escape(word)}\b", prompt_lower):
            score += 50
    for sensitive in SENSITIVE_INFO:
        if re.search(rf"\b{re.escape(sensitive)}\b", prompt_lower):
            score += 30

    # Stage 2: Contextual scoring using NLP
    doc = nlp(prompt)
    for token in doc:
        if token.dep_ in ["dobj", "pobj"] and token.head.lemma_ in DANGEROUS_KEYWORDS:
            score += 10
        # Detect imperative sentences
        if token.tag_ == "VB" and token.head.dep_ == "ROOT":
            score += 5

    # Cap risk at 100
    return min(score, 100)

def sanitize_input(prompt: str, user: str = ""):
    """
    Returns sanitized prompt and risk score.
    Can be extended with more advanced sanitization later.
    """
    risk_score = calculate_risk(prompt, user)
    sanitized_prompt = prompt  # In the future, you could remove/obfuscate risky content
    return sanitized_prompt, risk_score