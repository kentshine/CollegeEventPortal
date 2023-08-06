from datetime import datetime
from flask import render_template, url_for, redirect, request, Blueprint,flash,abort
from flask_login import current_user,login_required
from eventportal import db
from eventportal.models import Event,User
from eventportal.events.picture_handler import add_wallpaper,delete_wallpaper
from eventportal.events.event_registration import add_user,delete_records
from eventportal.events.email_handler import send_email
from eventportal.events.forms import CreateEventForm
from eventportal.registration import create_calendar_event,update_calendar_event
from eventportal import admin_id
from eventportal import background_threading

events = Blueprint('events',__name__)

@events.route('/create',methods=['GET','POST'])
def create():
    form = CreateEventForm()

    if form.validate_on_submit():
        calendar_id = create_calendar_event(title=form.title.data, description=form.description.data, location=form.location.data,date=form.event_date.raw_data[0], time=form.event_time.raw_data[0])
        event = Event(title=form.title.data,user_id=admin_id,location=form.location.data,event_date=form.event_date.raw_data[0],event_time=form.event_time.raw_data[0],description=form.description.data,calendar_id=calendar_id)
        if request.files['wallpaper']:
            wallpaper = request.files['wallpaper']
            event_name = form.title.data
            pic = add_wallpaper(wallpaper,event_name)
            event.wallpaper = pic

        '''
        title = request.form.get('title')
        location = request.form.get('location')
        event_date = request.form.get('date')
        event_time = request.form.get('time')
        description = request.form.get('description')
        '''

        ## event = Event(user_id=current_user.id,title=title,location=location,event_date=event_date,event_time=event_time,description=description)

        db.session.add(event)
        db.session.commit()
        print(event)
        next_page = request.args.get('next')
        if next_page is None or not next_page[0]=="/":
            next_page=url_for('core.index')
        return redirect(next_page)


    return render_template('create.html',form=form)

@events.route("/<int:event_id>",methods=["GET","POST"])
def event(event_id):
    event = Event.query.get_or_404(event_id)
    event_wallpaper = url_for('static',filename='event_wallpapers//'+event.wallpaper)
    if request.method == "POST":
        registered_before = False
        if  current_user.is_authenticated == False:
            flash("You need to have account to register !!")
        else:
            user = User.query.filter_by(id=current_user.id).first()
            for student in event.coming:
                if student.email == user.email:
                    registered_before = True
            if not registered_before:
                event.coming.append(user)
                db.session.commit()
                add_user(user.id,event.id)
                update_calendar_event(calendar_id='primary',event_id=event.calendar_id,new_guest=user.email)
                flash(send_email(event_id=event.id,user_id=user.id))
                redirect(url_for('core.index'))
                print(user.email , " has been registered to " , event.title)
            elif registered_before:
                flash("You are already registered !!")
                print(user.email, " has been already registered to ", event.title)
                redirect(url_for('events.event_listview'))
    return render_template("eventpage.html",id=event.id,title=event.title,location=event.location,event_date=event.event_date,event_time=event.event_time,description=event.description,event_wallpaper=event_wallpaper)

@events.route("/event-list")
def event_listview():
    page = request.args.get('page',1,type=int)
    events = Event.query.paginate(page=page,per_page=10)
    return render_template("MorePages.html",events=events)





'''
@events.route("/<int:event_id>/update",methods=['GET','POST'])
def update(event_id):
    form = CreateEventForm()
    event = Event.query.get_or_404(event_id)
    if form.validate_on_submit():   
        event.title = form.title.data
        event.location = form.location.data
        event.event_time = form.event_time.raw_data[0]
        event.event_date = form.event_date.raw_data[0]
        event.description = form.description.data

        if request.files['wallpaper']:
            wallpaper = request.files['wallpaper']
            event_name = event.title
            pic = add_wallpaper(wallpaper, event_name)
            event.wallpaper = pic

        db.session.commit()
        return redirect(url_for('events.event', event_id=event_id))



    elif request.method == "GET":
        form.title.data = event.title
        form.location.data = event.location
        form.event_time.data = datetime.strptime(event.event_time,'%H:%M')
        form.event_date.data = datetime.strptime(event.event_date,'%Y-%m-%d').date()
        form.description.data = event.description
   
    if request.method == "POST":
        event.title = request.form.get('title')
        event.location = request.form.get('location')
        event.event_date = request.form.get('date')
        event.event_time = request.form.get('time')
        event.description = request.form.get('description')
    return render_template('create.html',title='Update',form=form)
'''




'''
@events.route('/<int:event_id>/delete',methods=['POST','GET'])
def delete(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()

    next_page = request.args.get('next')
    if next_page is None or not request.args.get('next')[0]=="/":
        next_page = url_for('core.admin')

    return redirect(next_page)
'''



