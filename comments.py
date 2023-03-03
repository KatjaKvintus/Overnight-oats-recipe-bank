from db import db
from sqlalchemy.sql import text


def add_comment(user_id : int, recipe_id : int, comment_text : str):
    
    try:
        sql = text("""INSERT INTO comments (user_id, recipe_id, comment_text) 
                VALUES (:user_id, :recipe_id, :comment_text)""")

        db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "comment_text":comment_text})

        db.session.commit()

    except:
        return False

    return True


def show_comments(recipe_id):

    sql = text("SELECT DISTINCT " +
               "comments.*, users.name " +
               "FROM users " +
               "INNER JOIN comments ON (comments.user_id = users.id) " +
               "WHERE comments.recipe_id=:recipe_id")
    result = db.session.execute(sql, {"recipe_id":recipe_id})
    comment_items = result.fetchall()

    return comment_items