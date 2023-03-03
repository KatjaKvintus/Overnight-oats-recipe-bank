from app import app
from flask import redirect, render_template, request, session
import users
import recipes
import comments
from random import randint


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
    latest_recipe_items = recipes.show_latest_recipe()
    return render_template("mainpage.html", latest_recipe=latest_recipe_items)


@app.route("/search")
def search():   
    return render_template("search.html")


@app.route("/search_function", methods=["GET", "POST"])
def search_function():

    query1 = request.args["query1"]
    query2 = request.args["query2"]

    if query1 != None:
        list_of_search_matching_recipes = recipes.search_recipe_by_name(query1)
    elif query2 != None:
        list_of_search_matching_recipes = recipes.search_recipe_by_name(query2) 

    recipe_amount = len(list_of_search_matching_recipes)

    return render_template("search_results.html", recipe_amount=recipe_amount, list_of_search_matching_recipes=list_of_search_matching_recipes)


@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    return render_template("search_results.html")


# Displays individual recipe based in the id number
@app.route("/page", methods=["GET", "POST"])
def page():
    if request.method == "POST":
        id = request.form["this_is_recipe_id"]
        show_this_recipe = recipes.collect_recipe_items(id)
        recipe_comments = comments.show_comments(id)
    
    if len(recipe_comments) == 0:
        note = "No comments yet. Be the first one?"
    else:
        note = "Comments for this recipe: " + str(len(recipe_comments)) + " pcs"

    
    return render_template("recipe.html", id=id, show_this_recipe=show_this_recipe, recipe_comments=recipe_comments, note=note)


@app.route("/recipe_type", methods=["GET", "POST"])
def type():
    type = request.form["type"]    
    if type != None:
        list_of_search_matching_recipes = recipes.list_recipes_by_type(type)
        recipe_amount = len(list_of_search_matching_recipes)
        return render_template("search_results.html", recipe_amount=recipe_amount, list_of_search_matching_recipes=list_of_search_matching_recipes)


@app.route("/all_recipes", methods=["GET", "POST"])
def all_recipes():
    list_of_search_matching_recipes = recipes.get_all_recipes()
    recipe_amount = len(list_of_search_matching_recipes)
    return render_template("search_results.html", recipe_amount=recipe_amount, list_of_search_matching_recipes=list_of_search_matching_recipes)


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():
    if request.method == "GET":
        return render_template("add_new_recipe.html")
        
    if request.method == "POST":      
        name = request.form["name"]
        type = request.form["type"]
        author_id = users.get_user_id()
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


@app.route("/favorite", methods=["GET", "POST"])
def favorites():
    user_id = users.get_user_id()

    if request.method == "POST":
        recipe_id = request.form["favorite"]
        recipe_id = int(recipe_id)

    if recipes.mark_recipe_as_favorite(recipe_id, user_id):
        return "Favorite saved! (Click back button on your browser to return to the recipe.)"

    else:
        return render_template("error.html", message="Not succesfull")


@app.route("/my_favorites", methods=["GET", "POST"])
def my_favorites():
    user_id = users.get_user_id()
    list_of_search_matching_recipes = recipes.show_my_favorites(user_id)
    recipe_amount = len(list_of_search_matching_recipes)
    return render_template("search_results.html", recipe_amount=recipe_amount, list_of_search_matching_recipes=list_of_search_matching_recipes)


@app.route("/add_comment", methods=["GET", "POST"])
def add_comment():

    user_id = users.get_user_id()

    if request.method == "POST":
        new_comment = request.form["new_comment"]
        recipe_id = request.form["recipe_id"]
    
    result = comments.add_comment(user_id, recipe_id, new_comment)

    if not result:
        return render_template("error.html", message="Failed to add comment")
    else:
        return render_template("comment_saved.html")
    


@app.route("/random")
def random():

    amount_of_recipes = len(recipes.get_all_recipes())
    id = randint(1, amount_of_recipes)              # Random recipe id
    show_this_recipe = recipes.collect_recipe_items(id)
    recipe_comments = comments.show_comments(id)
    
    if len(recipe_comments) == 0:
        note = "No comments yet. Be the first one?"
    else:
        note = "Comments for this recipe: " + str(len(recipe_comments)) + " pcs"
    
    return render_template("recipe.html", id=id, show_this_recipe=show_this_recipe, recipe_comments=recipe_comments, note=note)




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
