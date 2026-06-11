from validate import validate_system
from repair import create_structure
import subprocess
import time
import sys

def run():

    print("LAW FIRM OS v8.6 — SYSTEM VALIDATION")

    result = validate_system()

    if result["status"] != "OK":
        print("SYSTEM INCOMPLETE")
        print(result["missing"])
        print("Running repair...")

        create_structure()

        print("Repair complete. Re-run installer.")
        return

    print("System OK")

    launch()

def launch():
    subprocess.Popen([
        "runtime/qdrant/qdrant.exe",
        "--storage-path",
        "runtime/qdrant_storage"
    ])

    time.sleep(2)

    subprocess.Popen([
        "runtime/python/python.exe",
        "-m",
        "streamlit",
        "run",
        "app/app.py"
    ])

if __name__ == "__main__":
    run()
