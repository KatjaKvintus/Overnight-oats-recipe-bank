from flask import Flask
from os import getenv
from sqlalchemy.sql import text


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


import routes
