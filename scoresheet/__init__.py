"""
Makes it so the scoresheet folder becomes a module
Can be run using Flask run or python3 main.py (wrkdir:root)
Creates database and application
"""


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """
    Creates the application
    Flask cors adds security
    Utilizes view.py for blueprint and routes
    Creates database
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lancelotdulac'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    CORS(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Game, Round, Player, Score

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    # Manage logins using the id of the current game
    @login_manager.user_loader
    def load_user(id):
        return Game.query.get(int(id))

    return app


def create_database(app):
    """ Creates a databse if it does not alredy exist """
    if not path.exists('scoresheet/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')


app = create_app()
