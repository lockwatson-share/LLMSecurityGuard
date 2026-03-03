def add_prompt(user, prompt, risk_score, provider):
    """Add prompt to queue.json"""
    import os, json
    QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.json")
    os.makedirs(os.path.dirname(QUEUE_FILE), exist_ok=True)
    try:
        with open(QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except:
        queue = []
    queue.append({"user": user, "prompt": prompt, "risk_score": risk_score, "provider": provider})
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def get_queue():
    import os, json
    QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.json")
    try:
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def mark_reviewed(index):
    import os, json
    QUEUE_FILE = os.path.join(os.path.dirname(__file__), "queue.json")
    queue = get_queue()
    if 0 <= index < len(queue):
        queue.pop(index)
        with open(QUEUE_FILE, "w") as f:
            json.dump(queue, f, indent=2)