from .base_adapter import LLMAdapter

class LocalAdapter(LLMAdapter):
    def send_prompt(self, prompt):
        return f"[LOCAL_MODEL] Response: {prompt[::-1]}"  # reversed string demo