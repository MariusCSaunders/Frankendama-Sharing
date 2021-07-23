from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Length

class FrankForm(FlaskForm):
    title = StringField("What is title of the setup?", validators=[InputRequired()])
    description = StringField("What is the description of your setup?", validators=[InputRequired()])
    tama = StringField("What type of tama?", validators=[InputRequired()])
    sarado = StringField("What type of sarado?", validators=[InputRequired()])
    sword = StringField("What type of sword?", validators=[InputRequired()])
    string = IntegerField("How long is the string in CM?", validators=[InputRequired(), NumberRange(min=1)])
    bearing = StringField("Does the setup have a bearing?", validators=[InputRequired(), Length(min=2, max=3)])
    companies = StringField("What companies are used? (Please seperate with a comma( , ))", validators=[InputRequired()])
    submit = SubmitField("Submit")
    

    #Attempted to make custom defined validators
    #def validate_string(self, string):
    #    if string.data < 1:
    #        raise ValidationError('Minimum is 1cm and maximum is "How long is a piece of string?"')

    #def validate_bearing(self, bearing):
    #   if bearing.data.lower() != "yes" or bearing.data.lower() != "no":
    #       raise ValidationError('Please enter Yes or No')

    