from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///kvintus"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["POST"])
def login():
    
    username = request.form["username"]
    password = request.form["password"]

    # Check if the username exists and matches with the password
    if login.log_in_user(username, password):
        session["username"] = username
        return redirect("/")


@app.route("/register")
def new_account():
    return render_template("register.html")

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")

@app.route("/admin_tools")
def admin_tools():
    return render_template("admin_tools.html")

@app.route("/exit")
def exit():
    return("Bye bye!")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])
