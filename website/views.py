"""
FILE TO STORE THE ROUTES/DIFFERENT PAGES THE USER CAN NAVIGATE TO.
"""

from flask import Blueprint

views = Blueprint('views', __name__)

# ROUTE FOR THE HOMEPAGE
@views.route('/')
def home():
    return "<h1>Test</h1>"


