from . import db

class Frankendama(db.Model):
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    tama = db.column(db.String(25), nullable=False)
    sarado = db.column(db.String(25), nullable=False)
    sword = db.column(db.String(25), nullable=False)
    string = db.column(db.String(25), nullable=False)
    bearing = db.Column(db.Boolean, nullable=False, default=True)
    company_id = db.column(db.Integer, db.ForeignKey('company_id'), nullable=False)


class Company(db.Model):
    company_id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(25), nullable=False)
    frankendama = db.Relationship('Frankendama', backref='Company')
