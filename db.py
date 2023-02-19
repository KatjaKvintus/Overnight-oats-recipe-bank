from os import getenv
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import session
from os import getenv


app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
