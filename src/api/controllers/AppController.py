from flask import Blueprint, render_template

blueprint = Blueprint("app", __name__, template_folder='templates')

@blueprint.route('/')
def index():
    return render_template("splash.html")
