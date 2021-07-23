#Marius Saunders
#QA Project 1
#Frankendama Sharing

#Imports all the needed modules
from application import db
from application.models import Company, Frankendama

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

#Creates entries in the Company database relating to the Frankendama entry above
company1 = Company(name = "CEREAL", frankendama_id = 1)
company2 = Company(name = "SK", frankendama_id = 1)


#Creates a Frankendama database entry
frank2 = Frankendama(
    title="Waves",
    description="A combo of damas with waves",
    tama="Black Waves 62mm",
    sarado="TJ kolsnik Kaizen",
    sword="TJ kolsnik Kaizen",
    string="58",
    bearing="Yes"
)

#Creates entries in the Company database relating to the Frankendama entry above
company3 = Company(name = "FRIDAY", frankendama_id = 2)
company4 = Company(name ="KUSA", frankendama_id = 2)
company5 = Company(name = "KUSA", frankendama_id = 2)

#Adds all the rows for both tables 
db.session.add(frank1)
db.session.add(frank2)
db.session.add(company1)
db.session.add(company2)
db.session.add(company3)
db.session.add(company4)
db.session.add(company5)

#Commits the changes
db.session.commit()