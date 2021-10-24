from flask import Flask
from application.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login_page'
login_manager.login_message = 'User need to be logged in'
login_manager.login_message_category = 'danger'

from application.content.home import home
from application.user.auth import auth
from application.user.profile import profile
from application.user.post import post

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(post)

