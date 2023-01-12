from flask import Flask

from src.api.controllers import AppController, UserController
from src.api.repositories.database import init_db

app = Flask(__name__)
app.register_blueprint(AppController.blueprint)
app.register_blueprint(UserController.blueprint)

init_db(app)
