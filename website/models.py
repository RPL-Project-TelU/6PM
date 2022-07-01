from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namaTeam = db.Column(db.String(64),index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    game = db.Column(db.String(64), index=True, nullable=False)