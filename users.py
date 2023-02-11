import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def user_id():
    return session.get("user_id", 0)


# Log in function for users that have an user account
def log_in_user(username, password):
        
    sql = text("SELECT id, password, role FROM users WHERE name=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        return False
    if not check_password_hash(user[2], password):
        return False
    
    session["user_id"] = user[1]
    session["user_name"] = username
    session["user_role"] = user[2]
    
    return True   


# Creates new user account and directs to login
def create_new_account(name, password):

    role = "user"

    if username_taken(name):
        return False

    hash_value = generate_password_hash(password)

    try:
        sql = """INSERT INTO users (name, password, role) 
                 VALUES (:name, :password, :role)"""

        db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    
    except:
        return False
    
    return log_in_user(name, password)


# Logging out of app 
def logout():
    del session["username"]



# Checks if suggested username is already in use. 
# Returns false if this username is unique.
def username_taken(username):

    sql = "SELECT name FROM users"
    result = db.session.execute(sql)
    list_of_usernames = result.fetchall()
    
    return username in list_of_usernames


def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]