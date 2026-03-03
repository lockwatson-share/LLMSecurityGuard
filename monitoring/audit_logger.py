import json, time

def log_event(user, prompt, response, risk_score, provider, mcp_verified):
    event = {
        "timestamp": int(time.time()),
        "user": user,
        "prompt": prompt,
        "response": response,
        "risk_score": risk_score,
        "provider": provider,
        "mcp_verified": mcp_verified
    }
    print("[AUDIT]", json.dumps(event, indent=2))