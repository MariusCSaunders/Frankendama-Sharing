from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Company, Frankendama


class TestBase(TestCase):

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI= "sqlite:///data.db"
        )

        return app

    
    def set_up(self):

        db.create_all()

        frank1 = Frankendama(
            title="Taps",
            description="A combo of damas designed for taps",
            tama="SK x Ceral STIK",
            sarado="Lomond Shape",
            sword="Lomond Shape",
            string="72",
            bearing="Yes"
        )

        company1 = Company(name = "CEREAL", frankendama_id = 1)
        company2 = Company(name = "SK", frankendama_id = 1)

        db.session.add(frank1)
        db.session.add(company1)
        db.session.add(company2)

        db.session.commit()

    
    def tear_down(self):

        db.drop_all()
