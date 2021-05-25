from datetime import datetime
from main import app, db, login_manager
from flask_login import UserMixin, current_user

# The below decorator reloads user from the client_id stored in the session

@login_manager.user_loader
def load_user(client_id):
    return Clients.query.get(int(client_id))

class Clients(db.Model, UserMixin):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable = False)
    lastName = db.Column(db.String(20), nullable = False)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(100), unique= True, nullable = False)
    mobile_number = db.Column(db.Integer, nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"Clients('{self.firstName}','{self.email}')"
