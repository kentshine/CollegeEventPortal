import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

######### DATABASE CONFIG ##############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

###################################
######### LOGIN CONFIG ############
###################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message = "Oui You are Logged In , hooray !!"
login_manager.login_message_category = "info"

###############################
###### BLUEPRINT CONFIGS ######
###############################

from eventportal.core.views import core
from eventportal.users.views import users
from eventportal.events.views import events
from eventportal.error_pages.handler import error_pages


# Register the app
app.register_blueprint(users)
app.register_blueprint(events)
app.register_blueprint(core)
app.register_blueprint(error_pages)