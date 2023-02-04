from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///kvintus"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/new_account")
def new_account():
    return render_template("register.html")

@app.route("/main_page")
def main_page():
    return render_template("main_page.html")

@app.route("/admin_tools")
def admin_tools():
    return("Tänne tulee pääkäyttäjän työkalut")

@app.route("/exit")
def exit():
    return("Bye bye!")

# For new pages
@app.route("/page/<int:id>")
def page(id):
    return "Tämä on sivu " + str(id)


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])
