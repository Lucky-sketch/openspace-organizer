from typing import List
from table import Table  
import random
import pandas as pd

class OpenSpace:
    def __init__(self, number_of_seats=4, number_of_tables=6):
        self.tables = [Table(number_of_seats) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables
        self.not_assigned = []  
        self.sum_of_places = 0  

    def organize(self, names: List[str]):
        random.shuffle(names)  
        for name in names:
            assigned = False

            sorted_tables = sorted(self.tables, key=lambda table: sum(1 for seat in table.seats if seat.free))
            
            for table in sorted_tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned = True
                    break

            if not assigned:
                self.not_assigned.append(name)
                print(f"No free spots available for {name}.")
            

    def display(self):
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

