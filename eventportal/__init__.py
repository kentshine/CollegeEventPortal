import os
from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from flask_mail import Mail,Message
from eventportal.models import User,Event
from eventportal.models import login_manager,basic_auth,db
from eventportal.models import EventView,UserView

app = Flask(__name__)
mail = Mail(app)

########## APP CONFIG #############
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = '1234'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jyothieventportal@gmail.com'
app.config['MAIL_PASSWORD'] = 'wquiwxnpegezlhjb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

## mail ###
mail = Mail(app)

######### DATABASE CONFIG ##############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app,db)

### Basic auth ###
basic_auth.init_app(app)



## admin ##
admin = Admin(app, name='eventportal', template_mode='bootstrap3')
admin.add_view(EventView(Event,db.session))
admin.add_view(UserView(User,db.session))






###################################
######### LOGIN CONFIG ############
###################################
login_manager.init_app(app)
login_manager.login_view = 'users.login'

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
