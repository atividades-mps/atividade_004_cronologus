from flask import Flask

from src.api.controllers import app_controller, user_controller
from src.api.repositories.database import init_db

app = Flask(__name__)
app.register_blueprint(app_controller.blueprint)
app.register_blueprint(user_controller.blueprint)

init_db(app)
