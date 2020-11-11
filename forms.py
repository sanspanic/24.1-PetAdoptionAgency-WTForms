from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange, Length


class AddPetForm(FlaskForm):
    """Form for adding new pets."""

    name = StringField("Pet Name", 
                        validators=[InputRequired()])

    species = SelectField("Species",
                        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField('Photo URL', 
                        validators=[Optional(), URL(require_tld=False)])

    age = IntegerField('Age', 
                        validators=[Optional(), NumberRange(min=0, max=30)])

    notes = StringField('Additional Notes', 
                        validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form for editing existing pets."""

    name = StringField("Pet Name", 
                        validators=[InputRequired()])

    photo_url = StringField('Photo URL', 
                        validators=[Optional(), URL(require_tld=False)])

    age = IntegerField('Age', 
                        validators=[Optional(), NumberRange(min=0, max=30)])

    notes = StringField('Additional Notes', 
                        validators=[Optional(), Length(min=10)])
    
    is_available = BooleanField("Is available?")

