
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager, current_user
#import mysql.connector

# new_db = mysql.connector.connect(host="localhost", user="root", passwd="$C0de1sco0L!", database="testdatabase")
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:$C0de1sco0L!@localhost/testdatabase'

db = SQLAlchemy()
DB_NAME = "database.db"


# Create a Flask Instance
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dj3!8rn*-q87b5mg$f0'
    # OLD DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    migrate = Migrate(app, db, render_as_batch=True)
    
    # INITIALIZE THE DATABASE BY PASSING IT OUR APP
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Course, Assignment, Submission, user_course

    with app.app_context():


        # userID = 3
        # user = User.query.filter(User.id == userID).first()
        # course = Course.query.filter(Course.teacher_id == userID).first()
        # courseID = course.id
        # courseCode = course.course_code

        # user.current_courses.append(course)

        # print("init Course:",course)
        # print("init CourseID:",courseID)
        # print("init CourseCode:",courseCode)
        # print("init course.enrolled_students:",course.enrolled_students)

        # print(user.current_courses)

        """
        QUERY TO LOOP OVER THE USERS IN A DATABASE AND RETURN THE NAMES
        AND EMAILS FOR ALL USERS
                users = User.query.filter().all()
                for user in users:
                    print(f"Name: {user.first_name} 
                    {user.last_name} - Email: {user.email}")
        """

        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

