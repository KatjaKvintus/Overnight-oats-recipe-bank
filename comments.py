from db import db
from sqlalchemy.sql import text


def add_comment(user_id : int, recipe_id : int, comment_text : str):

    print("DEBUD comments.py 1")#########################
    
    try:
        sql = text("""INSERT INTO comments (user_id, recipe_id, comment_text) 
                VALUES (:user_id, :recipe_id, :comment_text)""")

        print("DEBUD comments.py 2") #########################
        print("DEBUD comments.py 2.1: user_id on ", user_id) #########################
        print("DEBUD comments.py 2.2: recipe_id on ", recipe_id) #########################

        db.session.execute(sql, {"user_id":user_id, "recipe_id":recipe_id, "comment_text":comment_text})

        print("DEBUD comments.py 3")#########################

        db.session.commit()

        print("DEBUD comments.py 4")#########################

    except:
        print("DEBUD comments.py 5")#########################
        return False

    print("DEBUD comments.py 6 ")#########################

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