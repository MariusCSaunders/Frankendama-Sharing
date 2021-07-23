#Marius Saunders
#QA Project 1
#Frankendama Sharing

#Imports the needed modules
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
import os

from application import app, db
from application.models import Company, Frankendama

#Creates the base for all test cases
class TestBase(TestCase):

    # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

        return app
    
    #Testing method for setting up the test database
    def set_up(self):

        # Create table
        db.create_all()

        # Create test frankendama
        frank1 = Frankendama(
            title="Taps",
            description="A combo of damas designed for taps",
            tama="SK x Cereal STIK",
            sarado="Lomond Shape",
            sword="Lomond Shape",
            string="72",
            bearing="Yes"
        )

        # Create test companies
        company1 = Company(name = "CEREAL", frankendama_id = 1)
        company2 = Company(name = "SK", frankendama_id = 1)

        # Save Database entries 
        db.session.add(frank1)
        db.session.add(company1)
        db.session.add(company2)

        db.session.commit()


    #Testing method to destroy the testing database
    def tear_down(self):

        db.session.remove()
        db.drop_all()


#Testing method to test the loading of the three main pages works.
class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assert200(response)

    def test_update(self):
        response = self.client.get(url_for('update', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_home(self):
        response = self.client.get(
            url_for('home'),
            follow_redirects= True
            )

        assert "Taps" in response.data.decode()
        assert "Check updated task" in response.data.decode()
        assert "SK x Ceral STIK" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "72" in response.data.decode()
        assert "Yes" in response.data.decode()
        assert "CEREAL" in response.data.decode()
        assert "SK" in response.data.decode()

class TestUpdate(TestBase):

    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            data={"description": "Check updated task"},
            follow_redirects= True
        )

        assert "Taps" in response.data.decode()
        assert "Check updated task" in response.data.decode()
        assert "SK x Ceral STIK" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "72" in response.data.decode()
        assert "Yes" in response.data.decode()
        assert "CEREAL" in response.data.decode()
        assert "SK" in response.data.decode()

        assert "A combo of damas designed for taps" not in response.data.decode()


    def test_update_companies(self):
        response = self.client.post(
            url_for('update', id=1),
            data={"companies": "SWEETS"},
            follow_redirects= True
        )

        assert "Taps" in response.data.decode()
        assert "A combo of damas designed for taps" in response.data.decode()
        assert "SK x Ceral STIK" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "Lomond Shape" in response.data.decode()
        assert "72" in response.data.decode()
        assert "Yes" in response.data.decode()
        assert "SWEETS" in response.data.decode()
        assert "SK" not in response.data.decode()
        assert "CEREAL" not in response.data.decode()

class TestDelete(TestBase):

    def test_delete(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
        )

        assert "Taps" not in response.data.decode()
        assert "A combo of damas designed for taps" not in response.data.decode()
        assert "SK x Ceral STIK" not in response.data.decode()
        assert "Lomond Shape" not in response.data.decode()
        assert "Lomond Shape" not in response.data.decode()
        assert "72" not in response.data.decode()
        assert "Yes" not in response.data.decode()

