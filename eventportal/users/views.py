from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user
from eventportal import db
from eventportal.users.forms import LoginForm
from eventportal.models import User

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        department = request.form.get('department')
        semester = request.form.get('semester')
        print("this is email", email)
        print("this is password ", password)
        if User.query.filter_by(email=email).first() is not None:
            flash("Account with this email already exists !!")
            return redirect(url_for("users.register"))
        elif User.query.filter_by(email=email).first() is None:
            user = User(email=email, password=password,username=username,department=department,semester=semester)
            db.session.add(user)
            db.session.commit()
            flash("Thanks for registering! Now you can login!")
            print(user)
            return redirect(url_for('users.login'))

    return render_template('register.html')


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user is None:
            print("something wrong")
            flash("Email or password is incorrect")
            return render_template('login.html')


        elif user.check_password(password) and user is not None:
            login_user(user)
            next_page = request.args.get('next')

            if next_page is None or not next_page[0] == "/":
                next_page = url_for('core.index')

            flash("Logged in Successfully")
            print("Logged in as ", user)
            return redirect(next_page)
        else:
            flash("Password or Username is Incorrect")

    return render_template('login.html')


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))
