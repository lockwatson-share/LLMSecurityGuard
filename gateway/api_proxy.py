from flask import Flask, request, jsonify
from sanitizer.input_sanitizer import sanitize_input
from sanitizer.output_sanitizer import sanitize_output
from mcp_security.mcp_security import verify_context, sign_context, check_nonce
from manual_review.manual_review import add_prompt
import uuid
import time

app = Flask(__name__)

USER_TOKENS = {"demo_token": "demo_user"}

def local_llm_response(prompt: str):
    # Mock LLM response
    return f"[LOCAL_MODEL] Response: {prompt[::-1]}"

@app.route("/")
def home():
    return "LLMSecurityGuard API is running!"

@app.route("/llm", methods=["POST"])
def llm_endpoint():
    data = request.json
    token = request.headers.get("Authorization")

    if not token or token not in USER_TOKENS:
        return jsonify({"error": "Unauthorized"}), 401

    user = USER_TOKENS[token]
    prompt = data.get("prompt", "")
    signature = data.get("signature", "")
    nonce = data.get("nonce", "")
    timestamp = data.get("timestamp", int(time.time()))
    provider = data.get("provider", "local")

    # Verify nonce
    if not check_nonce(nonce):
        return jsonify({"error": "Replay attack detected"}), 400

    # MCP verification
    if not verify_context(prompt, user, signature, timestamp):
        return jsonify({"error": "Invalid MCP signature"}), 400

    # Input sanitization
    sanitized_prompt, input_risk = sanitize_input(prompt, user)

    # Risk scoring
    risk_score = max(input_risk, 0)

    # High-risk prompts → manual review
    if risk_score >= 50:
        add_prompt(user, sanitized_prompt, risk_score, provider)
        return jsonify({"risk_score": risk_score, "status": "pending_manual_review"})

    # LLM response
    llm_response = local_llm_response(sanitized_prompt)
    safe_response = sanitize_output(llm_response)

    return jsonify({
        "response": safe_response,
        "risk_score": risk_score,
        "status": "allowed"
    })

if __name__ == "__main__":
    app.run(debug=True)