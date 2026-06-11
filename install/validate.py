import os
import shutil
import subprocess

REQUIRED = [
    "runtime/qdrant/qdrant.exe",
    "app/app.py",
    "runtime/python/python.exe"
]

def check_files():
    missing = []

    for path in REQUIRED:
        if not os.path.exists(path):
            missing.append(path)

    return missing


def check_qdrant_running():
    try:
        result = subprocess.run(
            ["curl", "http://localhost:6333"],
            capture_output=True
        )
        return result.returncode == 0
    except:
        return False


def validate_system():
    missing = check_files()

    if missing:
        return {
            "status": "FAILED",
            "missing": missing
        }

    return {
        "status": "OK"
    }
