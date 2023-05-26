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

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        print("this is email" , email)
        print("this is password " , password)
        if User.query.filter_by(email=email).first() is not None:
            flash("Account with this email already exists !!")
            return redirect(url_for("users.register"))
        elif User.query.filter_by(email=email).first() is None:
            user = User(email=email,password=password)
            db.session.add(user)
            db.session.commit()
            flash("Thanks for registering! Now you can login!")
            print(user)
            return redirect(url_for('users.login'))
    return render_template('register.html')

@users.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user is None:
            flash("Email or password is incorrect")

        elif user.check_password(password) and user is not None:
            login_user(user)
            next_page=request.args.get('next')

            if next_page is None or not next_page[0] == "/":
                next_page = url_for('core.index')

            flash("Logged in Successfully")
            print("Logged in as " , user)
            return redirect(next_page)
    return render_template('login.html')

