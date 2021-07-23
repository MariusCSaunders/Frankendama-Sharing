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
        response = self.client.get(url_for('home'))
        assert "Taps" in response.data.decode()
        assert "A combo of damas designed for taps" in response.data.decode()
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

