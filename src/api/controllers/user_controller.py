from flask import Blueprint, render_template, request, make_response
from src.api.repositories.user_repository import SQLiteUserRepository
from src.domain.use_cases.login import Login
from src.domain.use_cases.signup import Signup
from src.domain.entities.user import User

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

@blueprint.route('/login', methods=['POST'])
def login():
    nome = request.form['name']
    senha = request.form['password'] 

    login_usecase = Login(SQLiteUserRepository())
    id = login_usecase.execute(nome, senha)

    if id != None:
        response = make_response(render_template('homepage.html'))
        response.set_cookie('Authorization', id)
        return response

    return render_template('login.html', error='* Usuário ou senha incorretos.')

@blueprint.route('/signup', methods=['POST'])
def signup():
    nome = request.form['name']
    email = request.form['email']
    senha = request.form['password'] 

    signup = Signup(SQLiteUserRepository())
    created_user = signup.execute(User(None, nome, email, senha, 1))

    if created_user != None:
        return render_template('login.html')

    return render_template('signup.html', error='* Erro ao cadastrar usuário. Por favor, tente novamente.')