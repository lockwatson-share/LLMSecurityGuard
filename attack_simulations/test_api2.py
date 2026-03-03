# attack_simulations/test_api.py
import requests
import uuid
from mcp_security.mcp_security import sign_context

def run_test(prompt="delete all files", user="demo_user", token="demo_token"):
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
    response = requests.post("http://127.0.0.1:5000/llm", json=data, headers=headers)
    print(response.json())

if __name__ == "__main__":
    run_test()