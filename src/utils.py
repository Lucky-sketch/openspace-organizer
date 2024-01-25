import json
import pandas as pd

def load_json():

    """Load configuration settings from a JSON file. """

    with open("src/config.json", "r") as f:
        config = json.load(f)
    return [config.get("number_of_seats"), config.get("number_of_tables")]

def xlsx_to_list(path):

    """ Read an Excel file and extract a list of names from the 'First Name' column."""

    df = pd.read_excel(path)
    return df['First Name'].tolist()
