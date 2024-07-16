from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flasknote.db"
app.config["SQLALCHEMY_TRACK_MODIFIFCATIONS"] = False

db = SQLAlchemy(app)