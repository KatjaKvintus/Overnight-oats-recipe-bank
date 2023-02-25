from db import db
from sqlalchemy.sql import text


def save_new_recipe(name, type, author_id, base_liquid, grain, protein, ingredient_1, ingredient_2, sweetener):

    try:
        sql = text("""INSERT INTO recipes (name, type, author_id, base_liquid, grain, 
                protein, ingredient_1, ingredient_2, sweetener) 
                VALUES (:name, :type, :author_id, :base_liquid, :grain, 
                :protein, :ingredient_1, :ingredient_2, :sweetener)""")

        db.session.execute(sql, {"name":name, "type":type, "author_id":author_id, "base_liquid":base_liquid, "grain":grain, "protein":protein, "ingredient_1":ingredient_1, "ingredient_2":ingredient_2, "sweetener":sweetener})
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


# Recipe search - work in progress
def search_recipe_by_name(keyword):
    sql = text("SELECT * FROM recipes WHERE name LIKE :keyword")
    result = db.session.execute(sql, {"keyword":"%"+keyword+"%"})
    recipes = result.fetchall()
    return recipes
