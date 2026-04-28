from models.movie import Movie
from models.Screen import Screen
from models.Showtime import Showtime
from models.Booking import Booking
from models.Eticket import Eticket

def run():
    # Create Movie
    movie = Movie(1, "Avengers", "Action", "English", 9, 180)

    # Create Screen
    screen = Screen(101, "Screen 1", 10)

    # Create Showtime (like doctor-patient relation)
    showtime = Showtime(1, movie, screen, "6:00 PM", "9:00 PM", 200)

    # Create Booking
    booking = Booking(1, "Shyam", showtime)

    # Select seats
    available_seats = screen.get_available_seats()
    booking.add_seat(available_seats[0])
    booking.add_seat(available_seats[1])

    # Confirm booking
    if booking.confirm_booking():
        ticket = Eticket(1, booking, "QR123")
        ticket.generate()

if __name__ == "__main__":
    run()
