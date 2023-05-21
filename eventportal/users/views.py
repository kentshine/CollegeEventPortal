from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from eventportal import db
from werkzeug.security import generate_password_hash,check_password_hash
from eventportal.users.forms import RegistrationForm, LoginForm
from eventportal.models import User

users = Blueprint('users', __name__)

@users.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering! Now you can login!")
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

@users.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully")

            next_page = request.args.get('next')

            if next_page is None or not next_page[0] == '/':
                next_page = url_for('core.index')

            return redirect(next_page)

    return render_template('login.html',form=form)

