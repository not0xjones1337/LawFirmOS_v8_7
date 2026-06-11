import subprocess

def ensure_model():
    print("Checking Ollama model...")

    subprocess.run(["ollama", "pull", "llama3.1"])

    print("Model ready")
