# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    create_at = db.Column(db.Integer)
    token = db.Column(db.String(32))

