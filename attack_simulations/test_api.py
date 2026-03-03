import requests
import uuid
from mcp_security.mcp_security import sign_context

prompt = "Hello LLM"
user = "demo_user"
nonce = str(uuid.uuid4())
signature, timestamp = sign_context(prompt, user)

data = {
    "prompt": prompt,
    "signature": signature,
    "nonce": nonce,
    "timestamp": timestamp,
    "provider": "local"
}

headers = {"Authorization": "demo_token"}
response = requests.post("http://127.0.0.1:5000/llm", json=data, headers=headers)
print(response.json())