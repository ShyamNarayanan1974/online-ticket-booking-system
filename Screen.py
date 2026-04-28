from models.Seat import Seat

class Screen:
    def __init__(self, screenId, name, totalSeats):
        self.screenId = screenId
        self.name = name
        self.seats = []

        for i in range(1, totalSeats + 1):
            self.seats.append(Seat(i, "A", i, "REGULAR", "AVAILABLE", None))

    def get_available_seats(self):
        return [seat for seat in self.seats if seat.is_available()]
