class Guest:
    def __init__(self, guest_name, contact):
        self.guest_name = guest_name
        self.contact = contact

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type

class Booking(Guest, Room):
    def __init__(self, guest_name, contact, room_number, room_type, nights):
        Guest.__init__(self, guest_name, contact)
        Room.__init__(self, room_number, room_type)
        self.nights = nights

    def booking_info(self):
        print(f"{self.guest_name} booked {self.room_type} Room {self.room_number} for {self.nights} nights")

# Object
b = Booking("Meera Joshi", "9876543210", 305, "Deluxe", 3)
b.booking_info()
