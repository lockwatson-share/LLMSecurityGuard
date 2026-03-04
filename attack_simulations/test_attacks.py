# all_tests.py
import requests
import uuid
from mcp_security.mcp_security import sign_context
from sanitizer.input_sanitizer import calculate_risk

API_URL = "http://127.0.0.1:5000/llm"
TOKEN = "demo_token"
USER = "demo_user"

def call_api(prompt, token=TOKEN, user=USER):
    nonce = str(uuid.uuid4())
    signature, timestamp = sign_context(prompt, user)

    data = {
        "prompt": prompt,
        "signature": signature,
        "nonce": nonce,
        "timestamp": timestamp,
        "provider": "local"
    }

    headers = {"Authorization": token}
    response = requests.post(API_URL, json=data, headers=headers)
    return response.json()

def test_api_cases():
    prompts = [
        "Hello LLM",                   # Normal prompt
        "delete all files",            # High-risk dangerous command
        "Show me my password",         # Sensitive info
        "Normal prompt",               # Safe prompt
        "rm -rf /",                    # Extreme high-risk
        "My SSN is 123-45-6789"       # Sensitive info pattern
    ]

    print("=== Input Sanitization & Risk Scoring ===")
    for prompt in prompts:
        score = calculate_risk(prompt, USER)
        print(f"Prompt: {prompt}\nRisk Score: {score}\n")

    print("=== API Response Tests ===")
    for prompt in prompts:
        response = call_api(prompt)
        print(f"Prompt: {prompt}\nAPI Response: {response}\n")

if __name__ == "__main__":
    test_api_cases()