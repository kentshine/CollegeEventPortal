import threading
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask import redirect,render_template,url_for,Response
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException


basic_auth = BasicAuth()
db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


registered = db.Table('registered',
                      db.Column('user_id',db.Integer,db.ForeignKey('users.id'),primary_key=True),
                      db.Column('event_id',db.Integer,db.ForeignKey('event.id'),primary_key=True)
                      )

class EventView(ModelView):
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        return redirect(url_for('events.create'))

class AuthException(HTTPException):
    def __init__(self,message):
        super().__init__(message,Response(
            message,401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class UserView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated. Refresh the page.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    event = db.relationship('Event', backref='creator', lazy=True)
    department = db.Column(db.String(64))
    semester = db.Column(db.String(64))
    registered_events = db.relationship('Event',secondary=registered,backref=db.backref('coming',lazy='dynamic'))


    def __init__(self, email, password,username,semester,department):
        self.username = username
        self.semester = semester
        self.department = department
        self.email = email
        self.password_hash = generate_password_hash(password)



    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Email: {self.email}"


class Event(db.Model):
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(140), nullable=False)
    event_date = db.Column(db.String,nullable=False)
    event_time = db.Column(db.String,nullable=False)
    location = db.Column(db.String,nullable=False)
    description = db.Column(db.Text, nullable=False)
    calendar_id = db.Column(db.String,nullable=False)
    wallpaper = db.Column(db.String,nullable=False,default="nothing.jpg")

    def __int__(self,user_id,title,event_date,event_time,location,description,calendar_id):
        self.user_id = user_id
        self.title = title
        self.event_date = event_date
        self.event_time = event_time
        self.location = location
        self.description = description
        self.calendar_id = calendar_id

    def __repr__(self):
        return f"Event Id: {self.id} --- Date: {self.event_date} --- Title: {self.title} --- Created By:{self.user_id}"



class NewThreadedTask(threading.Thread):
    def __init__(self):
        super(NewThreadedTask,self).__init__()

    def run(self):
        try:
            print("threaded task has been completed")
        except:
            print("Error Occured !!")
