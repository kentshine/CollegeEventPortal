import os
import csv
from pathlib import Path
from flask import current_app,url_for
from eventportal.models import User,Event
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from eventportal.registration import initialize


def add_user(user_id,event_id):
    event = Event.query.filter_by(id=event_id).first()
    user = User.query.filter_by(id=user_id).first()
    event_record_file = os.path.join(current_app.root_path,'static\event_records',str(event_id) + '.csv')
    fields_dict = {'Event ID':event.id,'Event Name':event.title,'Attendee':user.username,'Email':user.email,'Department':user.department,'Semester':user.semester}
    fields=['Event ID','Event Name','Attendee','Email','Department','Semester']
    if not os.path.isfile(event_record_file):
        with open(event_record_file,'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerow(fields_dict)

    else:
        with open(event_record_file,'a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=fields)
            writer.writerow(fields_dict)

    csvfile.close()

'''
def create_sheet(event):
    creds = initialize()
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                    fields='spreadsheetId') \
            .execute()
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

'''

def delete_records(event_id):
    event_record_file = os.path.join(current_app.root_path, 'static\event_records', str(event_id) + '.csv')
    with open(event_record_file,'r') as event_file:
        event_file.close()
    os.remove(event_record_file)

