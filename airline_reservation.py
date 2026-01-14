rows = 5
columns = 6

def initialize_seats():
    return [["O" for _ in range(columns)] for _ in range(rows)]

def display_seats(seats):
    print("\nSeat Layout (O = Available, X = Booked)")
    for row_index, row in enumerate(seats):
        print(f"Row {row_index + 1}: ", " ".join(row))


class Passenger:
    def __init__(self, name, seat_number, flight_code):
        self.name = name
        self.seat_number = seat_number
        self.flight_code = flight_code

    def __str__(self):
        return f"{self.name},{self.seat_number},{self.flight_code}"


def book_ticket(seats, passengers):
    name = input("Enter Name: ").strip()
    flight_code = input("Enter Flight Code: ").strip()

    display_seats(seats)

    row = int(input("Choose Row (1-5): ")) - 1
    col = int(input("Choose Column (1-6): ")) - 1

    if row < 0 or row >= rows or col < 0 or col >= columns:
        print("Invalid seat selection.")
        return

    if seats[row][col] == "O":
        seats[row][col] = "X"
        seat_number = f"{row+1}-{col+1}"
        passengers.append(Passenger(name, seat_number, flight_code))
        print("Booking Successful")
    else:
        print("Seat already booked.")


def search_passenger(passengers):
    keyword = input("Enter name to search: ").lower()
    found = False

    for p in passengers:
        if keyword in p.name.lower():
            print(p)
            found = True

    if not found:
        print("No Passengers Found.")


def cancel_booking(seats, passengers):
    seat = input("Enter Seat Number to Cancel (row-col): ")

    for p in passengers:
        if p.seat_number == seat:
            row, col = map(int, seat.split("-"))
            seats[row-1][col-1] = "O"
            passengers.remove(p)
            print("Booking Cancelled.")
            return

    print("Booking not found.")


def save_to_file(passengers):
    with open("booking_ticket.txt", "w") as file:
        for p in passengers:
            file.write(str(p) + "\n")


def load_from_file(seats, passengers):
    try:
        with open("booking_ticket.txt", "r") as file:
            for line in file:
                name, seat, flight = line.strip().split(",")
                passengers.append(Passenger(name, seat, flight))
                row, col = map(int, seat.split("-"))
                seats[row-1][col-1] = "X"
    except FileNotFoundError:
        pass


def main():
    seats = initialize_seats()
    passengers = []

    load_from_file(seats, passengers)

    while True:
        print("\n1. Book Ticket")
        print("2. View Seats")
        print("3. Cancel Booking")
        print("4. Search Passenger")
        print("5. Save & Exit")

        choice = input("Choose Option: ")

        if choice == "1":
            book_ticket(seats, passengers)
        elif choice == "2":
            display_seats(seats)
        elif choice == "3":
            cancel_booking(seats, passengers)
        elif choice == "4":
            search_passenger(passengers)
        elif choice == "5":
            save_to_file(passengers)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
