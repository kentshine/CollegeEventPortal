from eventportal.models import Event,User
from flask_mail import Message
from eventportal import db,mail


def send_email(event_id,user_id):
    event = Event.query.filter_by(id=event_id).first()
    user = User.query.filter_by(id=user_id).first()
    try:

        msg = Message(f'Thank you for registering for {event.title}', sender='jyothieventportal@gmail.com',
                      recipients=[user.email])
        msg.body = f"You are successfully registered for {event.title} on {event.event_date}"
        mail.send(msg)
        return "Successfully Registered"
    except:
        return "Failed to send email"
