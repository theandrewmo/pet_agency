from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField('Pet Name')
    species = StringField('Species', validators=[AnyOf(values=['dog','cat','porcupine'],message='dog, cat or porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='invalid age, must be between 0 and 30')])
    notes = StringField('Notes')
    available = BooleanField('Available')
    

