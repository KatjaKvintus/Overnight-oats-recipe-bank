from app import app
from flask import redirect, render_template, request, session
import login
import users
import recipes


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
        return render_template("error.html", message="Passwords don't match. Please type the sama password twice.")
    
    if not users.create_new_account(username, password1):
        return render_template("error.html", message="Failed to create user account")

    return redirect("/mainpage")


@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    #latest_recipe = recipes.show_latest_recipe()
    return render_template("mainpage.html")


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():

    if request.method == "GET":
        return render_template("add_new_recipe.html")
        
    if request.method == "POST":      
        name = request.form["name"]
        type = request.form["type"]
        author_id = users.user_id()
        base_liquid = request.form["base_liquid"]
        grain = request.form["grain"]
        protein = request.form["protein"]
        ingredient_1 = request.form["ingredient_1"]
        ingredient_2 = request.form["ingredient_2"]
        sweetener = request.form["sweetener"]

        result = recipes.save_new_recipe(name, type, author_id, base_liquid, grain, protein, ingredient_1, ingredient_2, sweetener)

        if not result:
            return render_template("error.html", message="Failed to save database.")
    
        return render_template("recipe_saved.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    
    #query = request.args["query"]
    #sql = "SELECT id FROM recipes WHERE content LIKE :query"
    #result = db.session.execute(sql, {"query":"%"+query+"%"})
    #recipe_search_result = result.fetchall()
    return render_template("search.html")


# For generating pages for individual recipes
@app.route("/page/<int:id>")
def page(id):
    return "Recipe number " + str(id)


@app.route("/admin_tools")
def admin_tools():
    return render_template("admin_tools.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    users.log_out()
    return render_template("logout.html")
