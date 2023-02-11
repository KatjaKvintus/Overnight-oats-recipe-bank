from app import app
from flask import redirect, render_template, request, session
import login
import users


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    # Check if the username exists and matches with the password
    if users.log_in_user(username, password):
        return ("Wrong username of password")

    session["username"] = username
    return redirect("/mainpage")


@app.route("/register", methods=["GET", "POST"])
def new_account():
    return render_template("register.html")


@app.route("/admin_tools")
def admin_tools():
    return render_template("admin_tools.html")

@app.route("/exit")
def exit():
    return("Bye bye!")

@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    return render_template("mainpage.html")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
