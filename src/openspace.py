from typing import List
from table import Table
import random
import pandas as pd

class OpenSpace:
    def __init__(self, number_of_seats=4, number_of_tables=6):

        """ Initialize an OpenSpace with a specified number of seats and tables. """

        self.tables = [Table(number_of_seats) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables
        self.not_assigned = []  # List to keep track of people not assigned to a seat
        self.sum_of_places = 0  # Total capacity left across all tables

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

    def display(self):

        """ Display the current seating arrangement and additional information."""

        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                if seat.free:
                    print(f"  Seat {j}: Empty")
                else:
                    print(f"  Seat {j}: {seat.occupant}")

        self.sum_of_places = sum(table.capacity_left() for table in self.tables)  # Update the sum directly
        print(f"Total capacity left: {self.sum_of_places}")
        print(f"Not assigned: {self.not_assigned}")
        print(f"The number of seats: {self.number_of_tables * table.capacity}")

    def store(self, filename: str):

        """ Store the seating arrangement and additional information in an Excel file. """
        
        data = {'Table': [], 'Seat': [], 'Occupant': []}

        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                data['Table'].append(f"Table {i}")
                data['Seat'].append(f"Seat {j}")
                data['Occupant'].append(seat.occupant if not seat.free else 'Empty')

        df = pd.DataFrame(data)
        df.loc[len(df)] = ["", "", f"Total seats: {self.number_of_tables * table.capacity}"]
        df.loc[len(df)] = ["", "", f"Total capacity left: {sum(table.capacity_left() for table in self.tables)}"]

        if self.not_assigned:
            df.loc[len(df)] = ["", "", f"Not assigned: {', '.join(self.not_assigned)}"]

        df.to_excel(filename, index=False)
