from flask import Flask
from .app import views

app = Flask(__name__)
app.register_blueprint(views.view)

