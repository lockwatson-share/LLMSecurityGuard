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

🚀 Features

MCP Security – Ensures integrity, replay protection, and auditability using HMAC signatures and nonces.

Authentication & RBAC – Token-based user authentication.

Input Sanitization – Detects dangerous commands and sensitive data.

Output Sanitization – Redacts emails, SSNs, and phone numbers.

Risk Scoring Engine – Scores prompts based on detected threats.

Manual Review Queue – High-risk prompts require human approval.

Interactive CLI Review Tool – Approve/reject prompts via terminal.

Streamlit Dashboard – Visual view of pending prompts.

Attack Simulations – Prebuilt scripts to test your security layers.

Modular Architecture – Easily extend with new sanitizers or adapters.

👥 Who Is This For?

Developers building LLM-powered apps

Security engineers auditing AI systems

DevSecOps professionals

Students & researchers learning LLM security

Startups exposing LLM APIs safely

🔐 Model Context Protocol (MCP)

MCP ensures:

Context Integrity – HMAC signatures prevent tampering

Replay Protection – Nonce validation blocks replay attacks

Authorization – Only valid tokens allowed

Auditability – Risk score & metadata tracked

Example MCP Signing
from mcp_security.mcp_security import sign_context
import uuid

prompt = "Hello LLM"
user = "demo_user"
nonce = str(uuid.uuid4())

signature, timestamp = sign_context(prompt, user)
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/<your-username>/LLMSecurityGuard.git
cd LLMSecurityGuard
2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Project
1️⃣ Start API Server
python gateway/api_proxy.py

API runs at:

http://127.0.0.1:5000/

Endpoints:

/ → Health check

/llm → Secure LLM gateway

2️⃣ Send a Test Prompt

All test scripts are located in:

attack_simulations/

Run:

python -m attack_simulations.test_api

High-risk prompt example:

prompt = "delete all files"

If risk ≥ 50:

{
  "risk_score": 50,
  "status": "pending_manual_review"
}
3️⃣ Interactive Manual Review CLI
python -m manual_review.cli

You can:

[a]pprove
[r]eject
[s]kip
[q]uit

Prompts are stored in:

manual_review/queue.json
4️⃣ Run Dashboard (Optional)
streamlit run dashboard/dashboard_app.py

View high-risk prompts visually at:

http://localhost:8501
5️⃣ Run Attack Simulations
python -m attack_simulations.test_attacks

Tests:

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

Contributions welcome!

You can:

Add new sanitizers

Improve risk scoring

Add LLM adapters

Improve dashboard

Expand attack simulations

📜 License

MIT License — see LICENSE file for details.