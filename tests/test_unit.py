from application import app, db
from application.models import Company, Frankendama
from flask import url_for
from flask_testing import TestCase


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )

        return app

    
    def setUp(self):
        
        #Destroys previous database and creates a new one
        db.drop_all()
        db.create_all()

        #Creates a Frankendama database entry
        frank1 = Frankendama(
            title="Taps",
            description="A combo of damas designed for taps",
            tama="SK x Cereal STIK",
            sarado="Lomond Shape",
            sword="Lomond Shape",
            string="72",
            bearing="Yes"
        )

        db.session.add(frank1)

        #Creates entries in the Company database relating to the Frankendama entry above
        company1 = Company(name = "CEREAL", frankendama_id = 1)
        company2 = Company(name = "SK", frankendama_id = 1)    
    
        db.session.add(company1)
        db.session.add(company2)
        db.session.commit()


    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)
        
    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assertEqual(response.status_code, 200)


class TestRead(TestBase):

    def test_read(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'Taps', response.data)
        self.assertIn(b'A combo of damas designed for taps', response.data)
        self.assertIn(b'SK x Cereal STIK', response.data)
        self.assertIn(b'Lomond Shape', response.data)
        self.assertIn(b'Lomond Shape', response.data)
        self.assertIn(b'72', response.data)
        self.assertIn(b'Yes', response.data)

        self.assertIn(b'CEREAL', response.data)
        self.assertIn(b'SK', response.data)

class TestUpdate(TestBase):

    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            follow_redirects= True,
            data = dict(
                title="Waves",
                description="A combo of damas with waves",
                tama="Black Waves 62mm",
                sarado="TJ kolsnik Kaizen",
                sword="TJ kolsnik Kaizen",
                string="58",
                bearing="Yes",
                companies="FRIDAY, kusa, KusA"
            )
        )

        self.assertIn(b'Waves',response.data)
        self.assertIn(b'A combo of damas with waves',response.data)
        self.assertIn(b'Black Waves 62mm',response.data)
        self.assertIn(b'TJ kolsnik Kaizen',response.data)
        self.assertIn(b'TJ kolsnik Kaizen',response.data)
        self.assertIn(b'58',response.data)
        self.assertIn(b'Yes',response.data)
        self.assertIn(b'FRIDAY',response.data)
        self.assertIn(b'KUSA',response.data)
        self.assertIn(b'KUSA',response.data)

class TestCreate(TestBase):

    def test_create(self):

        response = self.client.post(
        url_for('create'),
        follow_redirects= True,
        data = dict(
            title="Pizza",
            description="A combo of damas with pizzas",
            tama="62mm Boost Pizza",
            sarado="1.5",
            sword="TJ kolsnik Kaizen",
            string="62",
            bearing="Yes",
            companies="sweets, Cereal, CEREAL"
            )
        )

        self.assertIn(b'Pizza',response.data)
        self.assertIn(b'A combo of damas with pizzas',response.data)
        self.assertIn(b'62mm Boost Pizza',response.data)
        self.assertIn(b'1.5',response.data)
        self.assertIn(b'1.5',response.data)
        self.assertIn(b'62',response.data)
        self.assertIn(b'Yes',response.data)
        self.assertIn(b'SWEETS',response.data)
        self.assertIn(b'CEREAL',response.data)
        self.assertIn(b'CEREAL',response.data)

class TestDelete(TestBase):

    def test_delete(self):
             
        response = self.client.get(
        url_for('delete', id=1),
        follow_redirects=True
        )

        assert "Taps" not in response.data.decode()
        assert "A combo of damas designed for taps" not in response.data.decode()
        assert "SK x Cereal STIK" not in response.data.decode()
        assert "Lomond Shape" not in response.data.decode()
        assert "Lomond Shape" not in response.data.decode()
        assert "72" not in response.data.decode()
        assert "Yes" not in response.data.decode()
        assert "CEREAL" not in response.data.decode()
        assert "SK" not in response.data.decode()



    
