from .base_adapter import LLMAdapter

class ClaudeAdapter(LLMAdapter):
    def send_prompt(self, prompt):
        return f"[CLAUDE_SIM] Response: {prompt}"