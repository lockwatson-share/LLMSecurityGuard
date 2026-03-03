DANGEROUS_KEYWORDS = ["delete", "drop", "shutdown", "rm -rf", "exfiltrate"]
SENSITIVE_INFO = ["password", "secret", "ssn", "credit card"]

def calculate_risk(prompt: str, user: str = "") -> int:
    score = 0
    prompt_lower = prompt.lower()
    for word in DANGEROUS_KEYWORDS:
        if word in prompt_lower:
            score += 50
    for sensitive in SENSITIVE_INFO:
        if sensitive in prompt_lower:
            score += 30
    return min(score, 100)

def sanitize_input(prompt: str, user: str = ""):
    risk_score = calculate_risk(prompt, user)
    sanitized_prompt = prompt
    return sanitized_prompt, risk_score