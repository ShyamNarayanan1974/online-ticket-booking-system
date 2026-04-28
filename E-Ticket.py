class Eticket:
    def __init__(self, ticketId, booking, qrCode):
        self.ticketId = ticketId
        self.booking = booking
        self.qrCode = qrCode

    def generate(self):
        seat_numbers = [seat.number for seat in self.booking.seats]

        print("\n------ E-TICKET ------")
        print("Customer:", self.booking.customerName)
        print("Movie:", self.booking.showtime.movie.movieTitle)
        print("Screen:", self.booking.showtime.screen.name)
        print("Time:", self.booking.showtime.startTime)
        print("Seats:", seat_numbers)
        print("----------------------")
