from app.models.event import *

event_1 = Event("26-7-2025", "Foo Fighters", 160, "Wee Room", "Intimate up close and personal", False)
event_2 = Event("07-11-2020", "Tango night", 100, "Ballroom", "Intimate up close and personal, a night to remember!", True)
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)
