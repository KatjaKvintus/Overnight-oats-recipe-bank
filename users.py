import os
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


admin_key = "YouCantGuessTh1$"

def get_admin_key():
    return "YouCantGuessTh1$"

def get_user_id():
    return session.get("user_id", 0)


# Log in function for users that have an user account
def log_in_user(name, password):

    sql = text("SELECT id, password, role FROM users WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()

    if not user:
        return False

    if not check_password_hash(user[1], password):
        return False
    
    session["user_id"] = user[0]
    session["user_name"] = name
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()

    return True   


# Creates new user account and directs to login
def create_new_account(name, password, user_type):

    hash_value = generate_password_hash(password)
    role = user_type

    try:
        sql = text("""INSERT INTO users (name, password, role) 
                 VALUES (:name, :password, :role)""")

        db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    
    except:
        return False
    
    return log_in_user(name, password)


# Checks if suggested username is already in use. 
# Returns false if this username is unique.
def username_taken(username):

    sql = text("SELECT name FROM users")
    result = db.session.execute(sql)
    list_of_usernames = result.fetchall()
    
    return username in list_of_usernames


# Logging out of app 
def log_out():
    del session["user_id"]
    del session["user_name"]

