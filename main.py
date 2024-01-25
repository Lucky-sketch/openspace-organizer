import sys
sys.path.append('/Users/markshevchenkopu/BXL-Bouman-7/openspace-organizer/src')
from openspace import OpenSpace
import pandas as pd
from utils import load_json
import json

if __name__ == "__main__":

    def room_setup(path_to_the_file_with_colleagues, number_of_seats=4, number_of_tables=6):
        df = pd.read_excel(path_to_the_file_with_colleagues)
        mylist = df['First Name'].tolist()
        choice = input("Do you want to customize the setup? (Y/N): ").upper()
        if choice == "Y":
            choice_for_json = input("Do you want to import room setup from a JSON file? (Y/N): ").upper()

            if choice_for_json == 'Y':
                with open("src/config.json", "r") as f:
                    config = json.load(f)
                open_space = OpenSpace(number_of_seats=config.get("number_of_seats", 4),number_of_tables=config.get("number_of_tables", 6))
            else:
                number_of_tables = int(input('How many tables do you want? '))
                number_of_seats = int(input('How many seats do you want? '))
                open_space = OpenSpace(number_of_seats, number_of_tables)
        else:
            open_space = OpenSpace()

        open_space.organize(mylist)

        if len(open_space.not_assigned) > 0:
            choice2 = input('You have more people than tables, do you want to add tables? (Y/N): ').upper()
            if choice2 == "Y":
                new_number_of_tables = int(input('Enter the number of additional tables: '))
                open_space = OpenSpace(number_of_tables=open_space.number_of_tables + new_number_of_tables)
                open_space.organize(mylist)

        open_space.display()
        open_space.store("new.xlsx")

    room_setup("/Users/markshevchenkopu/BXL-Bouman-7/openspace-organizer/colleagues.xlsx")
