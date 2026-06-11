import os

def create_structure():
    folders = [
        "cases",
        "exports",
        "logs",
        "runtime/qdrant_storage"
    ]

    for f in folders:
        os.makedirs(f, exist_ok=True)

    return "STRUCTURE COMPLETE"
