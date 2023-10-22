from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
helloapp = Flask(__name__)
helloapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
helloapp.config['SECRET_KEY'] = 'this is my secret key'

db = SQLAlchemy(helloapp)
Migrate=Migrate(helloapp,db)
bcrypt=Bcrypt(helloapp)
login_manager=LoginManager(helloapp)
login_manager.login_view='login_page'
login_manager.login_message_category= 'info '


from market import routes  # Import 'routes' after creating 'helloapp' and 'db' instances

# Initialize the database
with helloapp.app_context():
    db.create_all()
