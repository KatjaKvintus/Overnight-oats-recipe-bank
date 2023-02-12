from app import app
from flask import redirect, render_template, request, session
import login
import users


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    # Check if the username exists and matches with the password
    if not users.log_in_user(username, password):
        return render_template("error.html", message="Incorrect username or password")
    
    return redirect("/mainpage")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
    
    if users.username_taken(username):
        return render_template("error.html", message="This username is taken. Please choose another one.")        

    if password1 != password2:
        return render_template("error.html", message="Passwords don't match. Please type the sama passwotd twice.")
    
    if not users.create_new_account(username, password1):
        return render_template("error.html", message="Failed to create user account")

    return redirect("/mainpage")


@app.route("/admin_tools")
def admin_tools():
    return render_template("admin_tools.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    return render_template("mainpage.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    users.log_out()
    return redirect("/login")
