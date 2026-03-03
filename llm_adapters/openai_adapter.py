from .base_adapter import LLMAdapter

class OpenAIAdapter(LLMAdapter):
    def send_prompt(self, prompt):
        return f"[OPENAI_SIM] Response: {prompt}"