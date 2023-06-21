from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template("error_pages/400.html",error_code=404,error_message="Page Not Found"),404

@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template("error_pages/400.html",error_code=403,error_message="Forbidden Access"),403

@error_pages.app_errorhandler(400)
def error_400(error):
    return render_template("error_pages/400.html",error_code=400,error_message="Bad Request"),400