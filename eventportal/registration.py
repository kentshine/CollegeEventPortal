from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/spreadsheets']


def initialize():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'eventportal/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def create_calendar_event(title, description, location, date, time):
    creds = initialize()

    try:
        service = build('calendar', 'v3', credentials=creds)
        event_date = f'{date}T{time}:00-00:00'
        print(event_date)
        event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {
                'dateTime': event_date,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': event_date,
                'timeZone': 'Asia/Kolkata',
            },
            'attendees': [{'email':'jyothieventportal@gmail.com'}],
            'reminders': {
                'useDefault':False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            }
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        # print('Event created: %s') % (event.get('htmlLink'))
        return event['id']


    except HttpError as error:
        print('An error occurred: %s' % error)


def list_events():
    creds = initialize()

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items',[])

        #printing events
        return events



    except HttpError as error:
        print('An error occurred: %s' % error)


def update_calendar_event(calendar_id,event_id,new_guest):
    creds = initialize()
    try:
        service = build('calendar', 'v3', credentials=creds)
        event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        print(event.keys())
        attendees = event['attendees']
        attendees.append({'email':new_guest})
        event['attendees'] = attendees
        updated_event = service.events().update(calendarId=calendar_id,eventId=event_id,body=event).execute()
        print(updated_event['updated'])
    except HttpError as error:
        print("An error occured: %s" % error)

'''
events = list_events()
for event in events:
    print(event['id'] , event['summary'])
'''


## update_event(calendar_id='primary',event_id='i21dpndpibuo46fgb8a9j75qg8',new_guest='genghiskhan@gmail.com')