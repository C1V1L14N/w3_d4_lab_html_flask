class Event():
    def __init__(self, date, event_name, num_of_guests, room_loc, description, recurring):
        self.date = date
        self.event_name = event_name
        self.num_of_guests = num_of_guests
        self.room_loc = room_loc
        self.description = description
        self.recurring = recurring