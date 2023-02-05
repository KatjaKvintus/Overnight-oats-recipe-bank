import os
import app
from db import db
from flask import request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

# Creates new user account and directs to login
def create_new_account(name, password, role):

    if is_username_unique(name):
        return False

    hash_value = generate_password_hash(password)

    try:
        sql = """INSERT INTO users (name, password, role) 
                 VALUES (:name, :password, :role)"""

        db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    
    except:
        return False
    
    return login(name, password)


# Log in function for existing username
def log_in_user(name, password):
    
    sql = "SELECT id, password, role FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()

    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    
    session["user_id"] = user[1]
    session["user_name"] = name
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()
    
    return True


# Logging out of app and ending sessions
def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]


# Checks if suggested username is already in use. 
# Returns false if this username is unique.
def is_username_unique(username):

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///kvintus"
    db = SQLAlchemy(app)
    result = db.session.execute("SELECT name FROM users")
    list_of_usernames = result.fetchall()
    
    return username in list_of_usernames
