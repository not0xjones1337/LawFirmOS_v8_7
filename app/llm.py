import subprocess

def run_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.1", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout
