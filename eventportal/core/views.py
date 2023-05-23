from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')

@core.route("/admin")
def admin():
    return render_template('admin.html')

@core.route('/info')
def info():
    return render_template('info.html')












