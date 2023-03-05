'''Module for handling recipe star reting related actions'''
from sqlalchemy.sql import text
from db import db


def give_stars(user_id, recipe_id, stars):
    '''Saves the recipe star rating from a single customer'''

    try:
        sql = text("""INSERT INTO upvotes (user_id, recipe_id, stars)
                VALUES (:user_id, :recipe_id, :stars)""")

        db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "stars":stars})
        db.session.commit()

    except SystemError:
        return False

    return True


def count_stars(recipe_id):
    '''Counts the star rating for individual recipe and the amount of revews given'''

    try:
        sql = text("""SELECT ROUND(SUM(stars)/COUNT(*), 1) AS stars_average,
         COUNT(*) AS amount_of_reviews FROM upvotes WHERE recipe_id = :recipe_id""")

        result = db.session.execute(sql, {"recipe_id":recipe_id})
        values = result.one()
        
    except SystemError:
        values = [0, 0]

    return values
