import json
import os


class FileReader:
    @staticmethod
    def load_json(path: str) -> dict:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        abs_path = os.path.join(base_dir, path)
        with open(abs_path, "r") as f:
            return json.load(f)

    @staticmethod
    def write_json(path:str,data:dict)->None:
        base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
        abs_path = os.path.join(base_dir, path)
        with open(abs_path, "w") as f:
            json.dump(data, f, indent=2)