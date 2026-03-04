LLMSecurityGuard

LLMSecurityGuard is an open-source secure gateway for LLM APIs. It helps developers, security engineers, and organizations safely deploy language models.

It provides:

Model Context Protocol (MCP) security

Authentication and Role-Based Access Control (RBAC)

Input and output sanitization

Risk scoring and manual review for high-risk prompts

Attack simulations

Dashboard monitoring

STRIDE-based threat modeling

Features

MCP Security: Ensures integrity, replay protection, and auditability using HMAC signatures and nonces.

Authentication & RBAC: Token-based user authentication and access control.

Input Sanitization: Detects dangerous commands and sensitive information.

Output Sanitization: Redacts emails, SSNs, phone numbers, and other sensitive data.

Risk Scoring Engine: Scores prompts based on detected threats.

Manual Review Queue: High-risk prompts require human approval.

Interactive CLI Review Tool: Approve or reject prompts via terminal.

Streamlit Dashboard: Visual view of pending prompts and risk metrics.

Attack Simulations: Prebuilt scripts to test security layers.

Modular Architecture: Easily extend with new sanitizers, adapters, or logging modules.

Who Is This For?

Developers building LLM-powered applications

Security engineers auditing AI systems

DevSecOps professionals

Students and researchers learning LLM security

Startups exposing LLM APIs safely

Model Context Protocol (MCP)

MCP ensures:

Context Integrity: HMAC signatures prevent tampering

Replay Protection: Nonce validation blocks replay attacks

Authorization: Only valid tokens are allowed

Auditability: Risk score and metadata tracked

Example: MCP Signing

from mcp_security.mcp_security import sign_context
import uuid

prompt = "Hello LLM"
user = "demo_user"
nonce = str(uuid.uuid4())

signature, timestamp = sign_context(prompt, user)

Send JSON to /llm API:
{
"prompt": prompt,
"signature": signature,
"nonce": nonce,
"timestamp": timestamp,
"provider": "local"
}

Note: Using OpenAI or Claude adapters requires API keys. For free testing, the local adapter is included.

Installation

Clone the repository:
git clone https://github.com/
<your-username>/LLMSecurityGuard.git
cd LLMSecurityGuard

Create a virtual environment:
python -m venv .venv

Mac/Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Install spaCy and English model for NLP input sanitization:
pip install spacy
python -m spacy download en_core_web_sm

Running the Project

Start the API Server:
python gateway/api_proxy.py

API runs at:
http://127.0.0.1:5000/

Endpoints:

/ → Health check

/llm → Secure LLM gateway

Send a Test Prompt:

All test scripts are located in attack_simulations/

Example:
python -m attack_simulations.test_api

High-risk prompt example:
prompt = "delete all files"

If risk ≥ 50, response:
{
"risk_score": 50,
"status": "pending_manual_review"
}

Interactive Manual Review CLI (Optional):
python -m manual_review.cli

CLI commands:
[a]pprove
[r]eject
[s]kip
[q]uit

Prompts are stored in: manual_review/queue.json

Run Dashboard (Optional):
streamlit run dashboard/dashboard_app.py

Open in browser (usually): http://localhost:8501

View high-risk prompts visually.

Run Attack Simulations:
python -m attack_simulations.test_attacks

Tests include:

Dangerous commands

Sensitive info requests

Normal prompts

Threat Model (STRIDE-Based)

Protected Against:

Prompt Injection

Context Tampering

Replay Attacks

Sensitive Data Leakage

Unauthorized API Access

Mitigations include:

HMAC signatures

Nonce validation

Risk scoring

Manual review workflow

Input/output sanitization

Project Structure

LLMSecurityGuard/

gateway/

sanitizer/

mcp_security/

manual_review/

dashboard/

attack_simulations/

requirements.txt

Contributing

Contributions are welcome! You can:

Add new sanitizers

Improve risk scoring

Add LLM adapters

Enhance dashboard or logging

Expand attack simulations

Follow code style and submit pull requests with clear descriptions.

License

MIT License — see LICENSE file for details.