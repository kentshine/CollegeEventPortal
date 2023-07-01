from flask import render_template, request, Blueprint
from eventportal.models import Event
from flask_login import current_user
core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    events = Event.query.order_by(Event.event_date.asc()).paginate(page=page,per_page=10)
    return render_template('index.html',events=events)



'''
@core.route("/admin")
def admin():
    page = request.args.get('page',1,type=int)
    events = Event.query.order_by(Event.event_date.asc()).paginate(page=page,per_page=4)
    return render_template('admin.html',events=events)
'''

@core.route('/info')
def info():
    return render_template('info.html')












