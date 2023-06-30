from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dj3!8rn*-q87b5mg$f0'

    from .views import views
    from .authentication import authentication

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    return app
