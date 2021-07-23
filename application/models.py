#Marius Saunders
#QA Project 1
#Frankendama Sharing

#Imports the needed modules
from . import db

#DB relationship is 1(Frankendama)-to-Many(Company)

#Frankendama table with all the defined columns
class Frankendama(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    tama = db.Column(db.String(25), nullable=False)
    sarado = db.Column(db.String(25), nullable=False)
    sword = db.Column(db.String(25), nullable=False)
    string = db.Column(db.String(25), nullable=False)
    bearing = db.Column(db.String(3), nullable=False)
    companies = db.relationship('Company', backref='frankendama', lazy=True)

#Company table with all the defined columns and Frankendama foreign Key
class Company(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    frankendama_id = db.Column(db.Integer, db.ForeignKey('frankendama.id'), nullable=False)
