from flask import request, session, abort


def login(username, password):

    database = "SELECT id, username, password, role FROM users WHERE username=:username"