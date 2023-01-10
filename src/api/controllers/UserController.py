from flask import Blueprint, render_template

blueprint = Blueprint("user", __name__, template_folder="templates")

@blueprint.route("/login")
def login_page():
    return render_template('login.html')

@blueprint.route("/signup")
def signup_page():
    return render_template('signup.html')

@blueprint.route("/homepage")
def home_page():
    return render_template('homepage.html')

@blueprint.route("/homepage/month")
def home_page_month():
    return render_template('homepage.html')

@blueprint.route("/homepage/week/<date>")
def home_page_week(date):
    return render_template('homepage-week.html', date=date)

@blueprint.route("/homepage/week")
def home_page_week_filter():
    return render_template('homepage-week.html')

@blueprint.route("/homepage/day/<date>")
def home_page_day(date):
    return render_template('homepage-day.html', date=date)

@blueprint.route("/homepage/day")
def home_page_day_filter():
    return render_template('homepage-day.html')

@blueprint.route('/login')
def login():
    return "ola"

@blueprint.route('/signup')
def signup():
    return "ola"