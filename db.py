from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User(id={self.id}, nickname={self.nickname})>"

class Upload(db.Model):
    __tablename__ = "uploads"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True, unique=True)
    data = db.Column(db.LargeBinary)

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data