from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class FrankForm(FlaskForm):
    title = StringField("What is title of the setup?")
    description = StringField("What is the description of your setup?")
    tama = StringField("What type of tama?")
    sarado = StringField("What type of sarado?")
    sword = StringField("What type of sword?")
    string = IntegerField("How long is the string in CM?")
    bearing = StringField("Does the setup have a bearing?")
    companies = StringField("What companies are used? (Please seperate with a comma( , ))")
    submit = SubmitField("Submit")
    


    