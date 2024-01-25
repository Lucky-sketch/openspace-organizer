import json
from openspace import OpenSpace

def load_json():
    with open("src/config.json", "r") as f:
        config = json.load(f)
    open_space = OpenSpace(number_of_seats=config.get("number_of_seats", 4),number_of_tables=config.get("number_of_tables", 6))