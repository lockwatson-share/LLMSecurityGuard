import hmac, hashlib, base64, time

USER_KEYS = {"demo_user": b"super_secret_mcp_key"}
used_nonces = set()
MAX_TIMESTAMP_DIFF = 300  # 5 minutes

def sign_context(prompt, user, timestamp=None):
    if user not in USER_KEYS:
        raise ValueError("Unknown user")
    timestamp = timestamp or int(time.time())
    message = f"{user}:{prompt}:{timestamp}".encode()
    signature = hmac.new(USER_KEYS[user], message, hashlib.sha512).digest()
    return base64.b64encode(signature).decode(), timestamp

def verify_context(prompt, user, signature, timestamp):
    expected_sig, _ = sign_context(prompt, user, timestamp)
    if abs(int(time.time()) - timestamp) > MAX_TIMESTAMP_DIFF:
        return False
    return hmac.compare_digest(expected_sig, signature)

def check_nonce(nonce):
    if nonce in used_nonces:
        return False
    used_nonces.add(nonce)
    return True