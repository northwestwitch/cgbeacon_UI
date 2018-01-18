from flask import Flask
from cgbeacon_UI import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Datasets(db.Model):

    __tablename__ = 'beacon_dataset_table'
    id = db.Column(db.String(50), primary_key=True)


class Variants(db.Model):

    __tablename__ = 'beacon_data_table'
    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.String(50),)
    chromosome = db.Column(db.String(2))
    position = db.Column(db.Integer)
    alternate = db.Column(db.String(100))
