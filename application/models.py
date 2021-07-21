from . import db

class Frankendama(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    tama = db.Column(db.String(25), nullable=False)
    sarado = db.Column(db.String(25), nullable=False)
    sword = db.Column(db.String(25), nullable=False)
    string = db.Column(db.String(25), nullable=False)
    bearing = db.Column(db.Boolean, nullable=False, default=True)
    #company_id = db.Column(db.Integer, db.foreignKey('company_id'), nullable=False)


#class Company(db.Model):
#    company_id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(25), nullable=False)
#    frankendama = db.relationship('Frankendama', backref='company')
