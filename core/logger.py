import os
from datetime import datetime

def log(message):
    base = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base, "logs")
    os.makedirs(log_dir, exist_ok=True)

    file = os.path.join(log_dir, "system.log")

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")


