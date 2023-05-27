from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import current_user,login_required
from eventportal import db
from eventportal.models import Event

events = Blueprint('events',__name__)

@events.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form.get('title')
        location = request.form.get('location')
        event_date = request.form.get('date')
        event_time = request.form.get('time')
        description = request.form.get('description')


        event = Event(user_id=current_user.id,title=title,location=location,event_date=event_date,event_time=event_time,description=description)
        db.session.add(event)
        db.session.commit()
        print(event)
        return redirect(url_for('core.index'))

    return render_template('create.html')

@events.route("/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event.html",title=event.title,location=event.location,event_date=event.event_date,event_time=event.event_time,description=event.description)

@events.route("/eventpage")
def event_view():
    return render_template('eventpage.html')

@events.route("/<int:event_id>/update",methods=['GET','POST'])
@login_required
def update(event_id):
    event = Event.query.get_or_404(event_id)
    if event.creator != current_user:
        abort(403)

    if request.method == "POST":
        title = request.form.get('title')
        location = request.form.get('location')
        event_date = request.form.get('date')
        event_time = request.form.get('time')
        description = request.form.get('description')
        return redirect(url_for('events.event',event_id=event_id))

    return render_template('create.html',title='Update')

@events.route('/<int:event_id>/delete',methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.creator != current_user:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('core.index'))