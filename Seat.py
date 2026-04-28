class Seat:
    def __init__(self, seatId, row, number, category, status, lockExpiry):
        self.seatId = seatId
        self.row = row
        self.number = number
        self.category = category
        self.status = status
        self.lockExpiry = lockExpiry

    def is_available(self):
        return self.status == "AVAILABLE"

    def book(self):
        self.status = "BOOKED"
