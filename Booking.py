class Booking:
    def __init__(self, bookingId, customerName, showtime):
        self.bookingId = bookingId
        self.customerName = customerName
        self.showtime = showtime
        self.seats = []
        self.status = "PENDING"

    def add_seat(self, seat):
        self.seats.append(seat)

    def confirm_booking(self):
        for seat in self.seats:
            if not seat.is_available():
                print("Seat not available")
                return False

        for seat in self.seats:
            seat.book()

        self.status = "CONFIRMED"
        print(f"Booking confirmed for {self.customerName}")
        return True
