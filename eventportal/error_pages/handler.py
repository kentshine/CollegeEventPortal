from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return "<h1> URL not found !! </h1>",404

@error_pages.app_errorhandler(403)
def error_403(error):
    return "<h1> YOU ARE FORBIDDEN HERE </h1>",403