import subprocess

def start_qdrant():
    print("Starting Qdrant...")

    subprocess.Popen([
        "docker", "run", "-p", "6333:6333", "qdrant/qdrant"
    ])

    print("Qdrant running at http://localhost:6333")
