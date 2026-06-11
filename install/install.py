import os
import shutil
import subprocess
from pathlib import Path

BASE = Path(os.environ["USERPROFILE"]) / "LawFirmOS"

def create_structure():
    folders = [
        BASE / "app",
        BASE / "runtime/qdrant",
        BASE / "cases",
        BASE / "exports"
    ]

    for f in folders:
        f.mkdir(parents=True, exist_ok=True)

def copy_payload():
    shutil.copytree("payload/app", BASE / "app", dirs_exist_ok=True)
    shutil.copytree("payload/runtime", BASE / "runtime", dirs_exist_ok=True)

def install_python_packages():
    subprocess.run([
        "pip", "install",
        "streamlit",
        "qdrant-client",
        "sentence-transformers",
        "pypdf",
        "python-docx",
        "reportlab"
    ])

def run():
    create_structure()
    copy_payload()
    install_python_packages()

    print("INSTALL COMPLETE")

if __name__ == "__main__":
    run()
