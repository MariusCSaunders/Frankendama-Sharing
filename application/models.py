from . import db

class Frankendama(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    tama = db.Column(db.String(25), nullable=False)
    sarado = db.Column(db.String(25), nullable=False)
    sword = db.Column(db.String(25), nullable=False)
    string = db.Column(db.String(25), nullable=False)
    bearing = db.Column(db.String(5), nullable=False)
    #company_id = db.Column(db.Integer, db.foreignKey('company_id'), nullable=False)
    companies = db.relationship('Company', backref='frankendama', lazy=True)


class Company(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    frankendama_id = db.Column(db.Integer, db.ForeignKey('Frankendama'), nullable=False)
