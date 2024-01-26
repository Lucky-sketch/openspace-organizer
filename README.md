# OpenSpace Organizer

The OpenSpace Organizer is a program designed to help you efficiently organize people in an open space by assigning them to seats at different tables. The program allows for customization of the setup and provides options to import configurations from JSON files or manually input the number of tables and seats. The program also create an excel file with all the information about open space organization that you may need to know. Program uses the algorithm that ensures that people are distributed equally among the tables, so everybody has a lot of fun:)

## Table of Contents

- [Prerequisites ](#prerequisites)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Interesting to know](#interesting_to_know)


## Prerequisites
#What you need to run the program

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/openspace-organizer.git
   cd openspace-organizer
   ```

2. Install all the needed libraries:
   ```bash
   pip install pandas
   pip install openpyxl
   ```

3. Update colleagues.xlsx Excel file with name of your colleagues


4. If you are going to configure setup with Json file than you also need to update ```config.json``` file with your room setup




## Usage

1. Configure the Setup
   
Run the main.py script to configure everything:

```bash
python3 main.py
```

You have 2 options to customize your setup (the number of tables and seats): manually or by importing it from a JSON file and other possibility is to continue with predefined one, anyway follow prompts to discover all the possibilities.

2. Organize the Open Space
Once the setup is configured, the program will organize the open space by assigning people to seats at tables. If there are more people than tables, you have the option to add more tables.

3. Display and Store Results
The organized open space will be displayed, showing the seating arrangement and additional information. The results will also be stored in an Excel file named ```new.xlsx```


## File Structure

```openspace.py``` Contains the OpenSpace class responsible for organizing people in the open space.
```table.py``` Defines the Table and Seat classes used to creating tables and seats instances.
```utils.py``` Contains functions for loading JSON configurations and reading Excel files.
```main.py``` The main script to run the OpenSpace Organizer.


## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.



## Interesting to know

This is the algorithm to assign people on the tables equally, basically it just calculates whether or not people can be divided evenly among all the tables, with this line ```remaining_people = len(names) % self.number_of_tables``` because when we have let's say 20 people and 10 tables then 20 % 10 = 0, so all the tables will have the same number of people. Program assigns people one by one and to make it this line that go through all the tables is applied: ```current_table = self.tables[table_index % self.number_of_tables]```. If there is such a number of people that it is impossible to distribute them equally extra people will be assigned to first tables due to this condition ```if table_index < remaining_people:
                                                     current_table = self.tables[table_index]
                                               ```

   ```
    def organize(self, names: List[str]):

        """ Organize people into seats at tables."""

        random.shuffle(names)  # Shuffle the list of names for randomness
        
        # Calculate the number of people to be assigned to each table
        remaining_people = len(names) % self.number_of_tables

        table_index = 0
        for name in names:
            # Determine the current table to assign the person to
            if table_index < remaining_people:
                current_table = self.tables[table_index]
            else:
                current_table = self.tables[table_index % self.number_of_tables]

            # Assign the person to a seat if available; otherwise, add to the not_assigned list
            if current_table.has_free_spot():
                current_table.assign_seat(name)
            else:
                self.not_assigned.append(name)
                print(f"No free spots available for {name}.")

            table_index += 1
   ```


## Good luck with using this program and enjoy organising your space
![giphy](https://github.com/Lucky-sketch/openspace-organizer/assets/53155116/b65c97c0-a6fb-4f24-b065-eb5fff5fc12d)







