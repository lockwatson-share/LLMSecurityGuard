LLMSecurityGuard

LLMSecurityGuard is an open-source secure gateway for LLM APIs, designed to help developers, security engineers, and organizations safely deploy language models.

It provides:

Model Context Protocol (MCP) security

Authentication & RBAC

Input/output sanitization

Risk scoring & manual review

Attack simulations

Dashboard monitoring

STRIDE-based threat modeling

Features

MCP Security – Ensures integrity, replay protection, and auditability using HMAC signatures and nonces.

Authentication & RBAC – Token-based user authentication and role-based access control.

Input Sanitization – Detects dangerous commands and sensitive data.

Output Sanitization – Redacts emails, SSNs, and phone numbers.

Risk Scoring Engine – Scores prompts based on detected threats.

Manual Review Queue – High-risk prompts require human approval.

Interactive CLI Review Tool – Approve/reject prompts via terminal.

Streamlit Dashboard – Visual view of pending prompts and risk metrics.

Attack Simulations – Prebuilt scripts to test your security layers.

Modular Architecture – Easily extend with new sanitizers, adapters, or logging modules.

Who Is This For?

Developers building LLM-powered apps

Security engineers auditing AI systems

DevSecOps professionals

Students & researchers learning LLM security

Startups exposing LLM APIs safely

Model Context Protocol (MCP)

MCP ensures:

Context Integrity – HMAC signatures prevent tampering

Replay Protection – Nonce validation blocks replay attacks

Authorization – Only valid tokens are allowed

Auditability – Risk score & metadata tracked

Example: MCP Signing

from mcp_security.mcp_security import sign_context
import uuid

prompt = "Hello LLM"
user = "demo_user"
nonce = str(uuid.uuid4())

signature, timestamp = sign_context(prompt, user)

# Send JSON to /llm API:
# {
#   "prompt": prompt,
#   "signature": signature,
#   "nonce": nonce,
#   "timestamp": timestamp,
#   "provider": "local"
# }

Note: Using OpenAI or Claude adapters requires API keys. For free testing, use the local adapter included in the project.

Installation

1) Clone Repository

git clone https://github.com/<your-username>/LLMSecurityGuard.git
cd LLMSecurityGuard

2) Create Virtual Environment

python -m venv .venv

# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

3) Install Dependencies

pip install -r requirements.txt
  Running the Project
1) Start API Server
python gateway/api_proxy.py

API runs at:

http://127.0.0.1:5000/

Endpoints:

/ → Health check

/llm → Secure LLM gateway

2) Send a Test Prompt

All test scripts are located in:

attack_simulations/

Example:

python -m attack_simulations.test_api

High-risk prompt example:

prompt = "delete all files"

If risk ≥ 50:

{
  "risk_score": 50,
  "status": "pending_manual_review"
}
3) Interactive Manual Review CLI (Optional)
python -m manual_review.cli

CLI commands:

[a]pprove

[r]eject

[s]kip

[q]uit

Prompts are stored in:

manual_review/queue.json
4) Run Dashboard (Optional)
streamlit run dashboard/dashboard_app.py

Open in browser (usually):

http://localhost:8501

View high-risk prompts visually.

5) Run Attack Simulations
python -m attack_simulations.test_attacks

Tests include:

Dangerous commands

Sensitive info requests

Normal prompts

🛡️ Threat Model (STRIDE-Based)

Protected Against:

Prompt Injection

Context Tampering

Replay Attacks

Sensitive Data Leakage

Unauthorized API Access

Mitigations:

HMAC signatures

Nonce validation

Risk scoring

Manual review workflow

Input/output sanitization

📁 Project Structure
LLMSecurityGuard/
├── gateway/
├── sanitizer/
├── mcp_security/
├── manual_review/
├── dashboard/
├── attack_simulations/
└── requirements.txt
🤝 Contributing

Contributions are welcome! You can:

Add new sanitizers

Improve risk scoring

Add LLM adapters

Enhance dashboard or logging

Expand attack simulations

Please follow the code style and submit pull requests with clear descriptions.

📜 License

MIT License — see LICENSE file for details.