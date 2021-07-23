from application import db
from application.models import Company, Frankendama

db.drop_all()
db.create_all()

first_frank = Frankendama(
    title="Waves",
    description="A combo of damas with waves",
    tama="Black Waves 62mm",
    sarado="TJ kolsnik Kaizen",
    sword="TJ kolsnik Kaizen",
    string="58",
    bearing="Yes"
)

company1 = Company(name = "FRIDAY", frankendama_id = 1)
company2 = Company(name ="KUSA", frankendama_id = 1)
company3 = Company(name = "KUSA", frankendama_id = 1)

db.session.add(first_frank)
db.session.add(company1)
db.session.add(company2)
db.session.add(company3)
db.session.commit()
