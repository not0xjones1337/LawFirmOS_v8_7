import os
import json
from core.logger import log


class CaseManager:

    def __init__(self, base_path="data/cases"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def create_case(self, case_id, name):

        path = os.path.join(self.base_path, case_id)

        os.makedirs(path, exist_ok=True)
        os.makedirs(os.path.join(path, "documents"), exist_ok=True)
        os.makedirs(os.path.join(path, "embeddings"), exist_ok=True)

        metadata = {
            "case_id": case_id,
            "name": name
        }

        with open(os.path.join(path, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)

        log(f"CASE CREATED: {case_id}")

        return path

    def list_cases(self):

        return os.listdir(self.base_path)

    def get_case_path(self, case_id):

        return os.path.join(self.base_path, case_id)
