import re

def sanitize_output(output: str) -> str:
    output = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[REDACTED_EMAIL]", output)
    output = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]", output)
    output = re.sub(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", "[REDACTED_PHONE]", output)
    return output