from icalendar import Calendar, Event
from datetime import datetime, timedelta
from random import randint
import csv

team = 'Hot Mess Express'

cal = Calendar()
cal.add('prodid', 'Tuesday Co-Ed Soccer Schedule')
cal.add('version', '0.1')

with open('schedule.csv') as csv_file:
    schedule = csv.DictReader(csv_file)

    for game in schedule:
        if game['Home'] != team and game['Away'] != team: continue
        event = Event()
        if game['Home'] == team:
            event.add('summary', 'Home Game vs {}'.format(game['Away']))
        else:
            event.add('summary', 'Away Game vs {}'.format(game['Home']))

        time = game['Date'] + " " + game['Start']
        time = datetime.strptime(time,  '%b %d, %Y %I:%M %p')
        event.add('dtstart', time)
        event.add('dtend', time + timedelta(0,3000))
        event.add('dtstamp', datetime.now())
        event.add('location', game['Facility'])
        event['uid'] = str(randint(1000000, 9999999))
        event.add('priority', 5)

        cal.add_component(event)

with open('schedule.ics', 'wb') as f:
    f.write(cal.to_ical())
