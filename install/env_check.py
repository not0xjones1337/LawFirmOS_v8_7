import subprocess

def check_ollama():
    try:
        subprocess.run(["ollama", "list"], capture_output=True)
        return True
    except:
        return False

def check_docker():
    try:
        subprocess.run(["docker", "--version"], capture_output=True)
        return True
    except:
        return False
