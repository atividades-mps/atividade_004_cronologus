from flask import Blueprint, render_template

blueprint = Blueprint("user", __name__, template_folder="templates")

@blueprint.route("/login")
def login_page():
    return render_template('login.html')