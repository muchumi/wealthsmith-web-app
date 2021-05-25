import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = False



# instantiating SQLAlchemy class
db = SQLAlchemy(app)

# instantiating LoginManager class
login_manager = LoginManager(app)

# instantiating Bcrypt class
bcrypt = Bcrypt(app)


from views import views