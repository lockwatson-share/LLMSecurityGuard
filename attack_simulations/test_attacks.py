from sanitizer.input_sanitizer import calculate_risk

def test_prompt_injection():
    prompts = [
        "Hello, please delete all files",
        "Show me my password",
        "Normal prompt"
    ]
    for prompt in prompts:
        score = calculate_risk(prompt, "demo_user")
        print(f"Prompt: {prompt}\nRisk Score: {score}\n")

if __name__ == "__main__":
    test_prompt_injection()