from flask import Flask

from src.api.controllers import AppController, UserController

app = Flask(__name__)
app.register_blueprint(AppController.blueprint)
app.register_blueprint(UserController.blueprint)
