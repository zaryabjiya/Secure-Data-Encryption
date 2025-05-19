# file_handler.py
import json
import os

def load_data(filename="stored_data.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data, filename="stored_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)
