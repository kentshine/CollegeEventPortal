import os
import csv
from flask import current_app,url_for
from eventportal.models import User,Event

## Adds user into an event
def add_user(user_id,event_id):
    event = Event.query.filter_by(id=event_id).first()
    user = User.query.filter_by(id=user_id).first()
    event_record_file = os.path.join(current_app.root_path,'static\event_records',event.title + '.csv')
    fields_dict = {'Event ID':event.id,'Event Name':event.title,'User':user.email}
    fields=['Event ID','Event Name','User']
    with open(event_record_file,'a') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fields)
        writer.writeheader()
        writer.writerow(fields_dict)


