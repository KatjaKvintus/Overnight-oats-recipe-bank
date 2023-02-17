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