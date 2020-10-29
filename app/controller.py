from app import app
from flask import render_template, request
from app.models.events_list import events, add_new_event
from app.models.event import *


@app.route('/')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route("/add-event", methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['event_name']
    event_guests = request.form['num_of_guests']
    room_loc = request.form['room_loc']
    event_desc = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_guests, room_loc, event_desc, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title="Home", events=events)
