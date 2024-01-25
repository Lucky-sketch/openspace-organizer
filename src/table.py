class Seat:
    def __init__(self, free: bool, occupant: str):

        """ Initialize a Seat with its occupancy status and occupant's name."""

        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):

        """ Assign a person to the seat if it is currently unoccupied. """

        if self.free:
            self.occupant = name
            self.free = False
            print(f"{name} has been assigned to the seat.")
        else:
            print("Seat is already occupied.")

    def remove_occupant(self):

        """ Remove the occupant from the seat if it is currently occupied."""

        if not self.free:
            occupant_name = self.occupant
            self.free = True
            self.occupant = None
            print(f"{occupant_name} has been removed from the seat.")
            return occupant_name
        else:
            print("Seat is already empty.")


class Table:
    def __init__(self, capacity):

        """Initialize a Table with a specified seating capacity. """

        self.capacity = capacity
        self.seats = [Seat(free=True, occupant="") for _ in range(capacity)]

    def has_free_spot(self):

        """ Check if there is at least one free seat at the table. """

        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):

        """ Assign a person to the first available free seat at the table. """

        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break
        else:
            print("No free spots available at this table.")

    def capacity_left(self):

        """ Get the number of free seats remaining at the table. """
        
        return sum(seat.free for seat in self.seats)
