class Seat:
    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            print(f"{name} has been assigned to the seat.")
        else:
            print("Seat is already occupied.")

    def remove_occupant(self):
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
        self.capacity = capacity
        self.seats = [Seat(free=True, occupant="") for x in range(capacity)]


    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break
        else:
            print("No free spots available at this table.")

    def capacity_left(self):
        return sum(seat.free for seat in self.seats)

