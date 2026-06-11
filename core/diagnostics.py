import os

def run_diagnostics():
    """
    Checks core system folders and returns list of issues.
    Empty list = system OK
    """

    issues = []

    base = os.path.dirname(os.path.dirname(__file__))

    required_paths = [
        os.path.join(base, "logs"),
        os.path.join(base, "data"),
        os.path.join(base, "core"),
    ]

    for path in required_paths:
        if not os.path.exists(path):
            issues.append(f"Missing path: {path}")

    return issues

