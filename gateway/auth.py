import time
from functools import wraps
from flask import request, jsonify

TOKENS = {"demo_token": "demo_user"}
RATE_LIMIT = {"demo_user": {"count": 0, "last_reset": time.time()}}
MAX_REQUESTS = 10
RESET_INTERVAL = 60  # seconds

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token not in TOKENS:
            return jsonify({"message": "Token missing or invalid"}), 403
        user = TOKENS[token]

        # Rate limiting
        now = time.time()
        if now - RATE_LIMIT[user]["last_reset"] > RESET_INTERVAL:
            RATE_LIMIT[user]["count"] = 0
            RATE_LIMIT[user]["last_reset"] = now
        RATE_LIMIT[user]["count"] += 1
        if RATE_LIMIT[user]["count"] > MAX_REQUESTS:
            return jsonify({"message": "Rate limit exceeded"}), 429

        return f(user, *args, **kwargs)
    return decorated