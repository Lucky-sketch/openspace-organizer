import sys
sys.path.append('src/')
from openspace import OpenSpace
from utils import load_json, xlsx_to_list

if __name__ == "__main__":
    # Read data from an Excel file
    path_to_the_file_with_colleagues = "colleagues.xlsx"
    mylist = xlsx_to_list(path_to_the_file_with_colleagues)

    # Customize the setup
    choice = input("Do you want to customize the setup? (Y/N): ").upper()

    if choice == "Y":
        choice_for_json = input("Do you want to import room setup from a JSON file? (Y/N): ").upper()

        if choice_for_json == 'Y':
            # Import room setup from a JSON file
            open_space = OpenSpace(number_of_seats=load_json()[0], number_of_tables=load_json()[1])
        else:
            # Manually input the number of tables and seats
            number_of_tables = int(input('How many tables do you want? '))
            number_of_seats = int(input('How many seats do you want? '))
            open_space = OpenSpace(number_of_seats, number_of_tables)
    else:
        # Use default setup
        open_space = OpenSpace()

    # Organize the open space
    open_space.organize(mylist)

    if len(open_space.not_assigned) > 0:
        # Add tables if there are more people than tables
        choice2 = input('You have more people than tables, do you want to add tables? (Y/N): ').upper()
        if choice2 == "Y":
            new_number_of_tables = int(input('Enter the number of additional tables: '))
            open_space = OpenSpace(number_of_tables=open_space.number_of_tables + new_number_of_tables)
            open_space.organize(mylist)

    # Display the organized open space
    open_space.display()

    # Store the results in a "new.xlsx" Excel file
    choice3 = input("Do you want to store your open-space inforamtion in the excel file? (Y/N): ").upper()
    if choice3 == "Y":
        open_space.store("new.xlsx")
