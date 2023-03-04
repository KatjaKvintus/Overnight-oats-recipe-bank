from db import db
from sqlalchemy.sql import text


# Saves the recipe star rating from a single customer
def give_stars(user_id, recipe_id, stars):

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

    try:
        sql = text("SELECT ROUND(SUM(stars)/COUNT(*), 1) AS stars_average, COUNT(*) AS amount_of_reviews FROM upvotes WHERE recipe_id = :recipe_id")
        result = db.session.execute(sql, {"recipe_id":recipe_id})
        values = result.one()
    except:
        values = [0, 0]

    return values