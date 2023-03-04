from db import db
from sqlalchemy.sql import text
from datetime import date


def save_new_recipe(name, type, author_id, base_liquid, grain, protein, ingredient_1, ingredient_2, sweetener):

    try:
        sql = text("""INSERT INTO recipes (name, type, author_id, base_liquid, grain, 
                protein, ingredient_1, ingredient_2, sweetener) 
                VALUES (:name, :type, :author_id, :base_liquid, :grain, 
                :protein, :ingredient_1, :ingredient_2, :sweetener)""")

        db.session.execute(sql, {"name":name, "type":type, "author_id":author_id, 
                                 "base_liquid":base_liquid, "grain":grain, "protein":protein, 
                                 "ingredient_1":ingredient_1, "ingredient_2":ingredient_2, 
                                 "sweetener":sweetener})
        db.session.commit()

    except:
        return False

    return True


# Returns a list of all recipes in the database
def get_all_recipes():
    sql = text("SELECT * FROM recipes")
    result = db.session.execute(sql)
    recipe_list = result.fetchall()
    return recipe_list


# Returns a list of individual recipe items
def collect_recipe_items(id):
    sql = text("SELECT * FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    recipe_items = result.fetchone()
    return recipe_items


# Collects idividual items from the newest recipe
def show_latest_recipe():
    list = get_all_recipes()
    recipe_id = len(list)
    return collect_recipe_items(recipe_id)


# Recipe search from recipe names
def search_recipe_by_name(keyword):
    keyword = keyword.lower()
    sql = text("SELECT * FROM recipes WHERE LOWER(name) LIKE :keyword")
    result = db.session.execute(sql, {"keyword":"%"+keyword+"%"})
    recipes = result.fetchall()
    return recipes


# Recipe search based on ingredient
def search_from_ingredients(keyword):
    keyword = keyword.lower()
    sql = text("SELECT * FROM recipes WHERE LOWER(base_liquid) LIKE :keyword "+
               "OR LOWER(grain) LIKE :keyword "+
               "OR LOWER(protein) LIKE :keyword "+
               "OR LOWER(ingredient_1) LIKE :keyword "+
               "OR LOWER(ingredient_2) LIKE :keyword "+
               "OR LOWER(sweetener) LIKE :keyword")
    result = db.session.execute(sql, {"keyword":"%"+keyword+"%"})
    recipes = result.fetchall()
    return recipes


# Recipe listing by type
def list_recipes_by_type(type):
    type = type.lower()
    sql = text("SELECT * FROM recipes WHERE LOWER(type) LIKE :type")
    result = db.session.execute(sql, {"type":"%"+type+"%"})
    recipes = result.fetchall()
    return recipes


# To mark a recipe as a favorite > added to favorites list
# Note: toggling the icon DOES NOT remove the recipe from favorites
def mark_recipe_as_favorite(recipe_id : int, user_id : int):

    try:
        sql = text("""INSERT INTO favorites (user_id, recipe_id) 
        VALUES (:user_id, :recipe_id)""")
        db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id})
        db.session.commit()

    except:
        return False
    return True

# Returns list of users favorites recipes
def show_my_favorites(user_id):

    try:
        sql = text("SELECT DISTINCT "+
                   "recipes.* "+
                   "FROM favorites "+
                   "INNER JOIN recipes ON (favorites.recipe_id = recipes.id) " +
                   "WHERE favorites.user_id = :user_id")

        result = db.session.execute(sql, {"user_id":user_id})
        favorite_list = result.fetchall()

    except:
        return "Error - no favorites found"

    return favorite_list


# Admin function: one of the database recipes can be set as the recipe of the week
def set_recipe_of_the_week(recipe_id):

    this_date = str(date.today())

    try:
        sql = text("""INSERT INTO recipe_of_the_week (recipe_id, date) 
                VALUES (:recipe_id, :date)""")

        db.session.execute(sql, {"recipe_id":recipe_id, "date":this_date})
        db.session.commit()

    except:
        return False

    return True


# Checks recipe_of_the_week tables lastest entry 
# and returns the id of that recipe in recipes table
def get_index_for_the_latest_recipe_of_the_week():

    sql = text("SELECT max(id) AS id FROM recipe_of_the_week")
    result = db.session.execute(sql)
    this_recipe = result.fetchone()
    this_recipe_id = this_recipe[0]

    sql = text("SELECT DISTINCT recipes.* " +
                "FROM recipe_of_the_week " +
                "INNER JOIN recipes ON (recipe_of_the_week.recipe_id = recipes.id) " +
                "WHERE recipe_of_the_week.id = :this_recipe_id")

    result = db.session.execute(sql, {"this_recipe_id":this_recipe_id})
    recipe = result.fetchone()

    if len(recipe) == 0:
        return 0
    else: 
        index_of_the_latest_one = recipe[0]
        return index_of_the_latest_one


# Saves the recipe star rating from a single customer
def give_stars(user_id, recipe_id, stars : int):

    try:
        sql = text("""INSERT INTO upvotes (user_id, recipe_id, stars) 
                VALUES (:user_id, :recipe_id, :stars)""")

        db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "stars":stars})
        db.session.commit()

    except:
        return False

    return True

# Counts the star rating for individual recipe and the amount of revews given
def count_stars(recipe_id):

    sql = text("SELECT ROUND(SUM(stars)/COUNT(*), 1) AS stars_average, COUNT(*) AS amount_of_reviews FROM upvotes WHERE recipe_id LIKE :recipe_id")
    result = db.session.execute(sql, {"recipe_id":recipe_id})
    values = result.fetchall()

    return values