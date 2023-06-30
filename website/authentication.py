

from flask import Blueprint

authentication = Blueprint('authentication', __name__)

@authentication.route('/login')
def login():
    return "<p>Login</p>"


@authentication.route('/logout')
def logout():
    return "<p>Logout</p>"


@authentication.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

