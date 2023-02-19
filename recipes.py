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


def get_all_recipes():

    sql = text("SELECT * FROM recipes")
    result = db.session.execute(sql)
    recipe_list = result.fetchall()
    return recipe_list


def recipe_to_string(id):
    sql = text("SELECT * FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    recipe = result.fetchone()

    # DEBUGGING ######################################
    print("Recipe-listan pituus: " + str(len(recipe)))
    print("Recipe-listan sisältö: ")
    for item in recipe:
        print(item)

    print(f"""
    {recipe[0]}\n
    Type: {recipe[2]}\n\n
    Ingredients:\n
    1 dl {recipe[4]}
    1 dl {recipe[5]}
    0,25 - 0,5 dl {recipe[6]}
    {recipe[7]}
    {recipe[8]}
    {recipe[9]}
    
    Peel and chop/grate fruits/vegetables.
    Add all ingredients to the bowl and mix well. 
    Cover the bowl with a lid and keep in a refridgerator 1-2 hours or over night.
    Enjoy!
    """)

def show_latest_recipe():
    list = get_all_recipes()
    recipe_id = len(get_all_recipes()) - 1
    recipe_to_string(recipe_id)

