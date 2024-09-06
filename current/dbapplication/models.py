from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    passowrd = db.Column(db.String, nullable=False)  # Corrected the typo here
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'
    
    def get_id(self):
        return str(self.uid)  # Flask-Login expects `get_id()` to return a string
