from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import current_user,login_required
from eventportal import db
from eventportal.models import Event
from eventportal.events.picture_handler import add_wallpaper

events = Blueprint('events',__name__)

@events.route('/create',methods=['GET','POST'])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get('title')
        location = request.form.get('location')
        event_date = request.form.get('date')
        event_time = request.form.get('time')
        description = request.form.get('description')



        event = Event(user_id=current_user.id,title=title,location=location,event_date=event_date,event_time=event_time,description=description)

        if request.files['wallpaper']:
            wallpaper = request.files['wallpaper']
            event_name = title
            pic = add_wallpaper(wallpaper,event_name)
            event.wallpaper = pic

        db.session.add(event)
        db.session.commit()
        print(event)
        next_page = request.args.get('next')
        if next_page is None or not next_page[0]=="/":
            next_page=url_for('core.admin')
        return redirect(next_page)

    return render_template('create.html')

@events.route("/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    event_wallpaper = url_for('static',filename='event_wallpapers//'+event.wallpaper)
    return render_template("eventpage.html",title=event.title,location=event.location,event_date=event.event_date,event_time=event.event_time,description=event.description,event_wallpaper=event_wallpaper)

@events.route("/event-list")
def event_listview():
    page = request.args.get('page',1,type=int)
    events = Event.query.paginate(page=page,per_page=10)
    return render_template("MorePages.html",events=events)

@events.route("/<int:event_id>/update",methods=['GET','POST'])
def update(event_id):
    event = Event.query.get_or_404(event_id)

    if request.method == "POST":
        title = request.form.get('title')
        location = request.form.get('location')
        event_date = request.form.get('date')
        event_time = request.form.get('time')
        description = request.form.get('description')
        db.session.commit()
        return redirect(url_for('events.event',event_id=event_id))

    return render_template('create.html',title='Update')

@events.route('/<int:event_id>/delete',methods=['POST','GET'])
def delete(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()

    next_page = request.args.get('next')
    if next_page is None or not request.args.get('next')[0]=="/":
        next_page = url_for('core.admin')

    return redirect(next_page)

