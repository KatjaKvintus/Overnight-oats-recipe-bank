import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text


def user_id():
    return session.get("user_id", 0)


# Log in function for users that have an user account
def log_in_user(name, password):
    
    #Debugging **************************************************************
    print("DEBUG 1: name on ", name, " ja salasana on ", password)

    sql = text("SELECT id, password, role FROM users WHERE name=:name")
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    password_in_table = user[1]

    #Debugging **************************************************************
    print("DEBUG 2: User on ", user)

    if not check_password_hash(user[1], password):
        return False
    
    session["user_id"] = user[0]
    #Debugging **************************************************************
    print("DEBUG 3: user_id on ", user[0], " ja salasana on ", password_in_table)


    session["user_name"] = name
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()
    
    #Debugging **************************************************************
    session_user_name = session["user_name"]
    session_user_role = session["user_role"]

    print("session_user_name on ", session["user_name"])
    print("session_user_role on ", session["user_role"])

    return True   


# Creates new user account and directs to login
def create_new_account(name, password):

    hash_value = generate_password_hash(password)
    role = "user"

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
    del session["user_role"]