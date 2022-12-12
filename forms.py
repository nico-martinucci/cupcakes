from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddCupcakeForm(FlaskForm):
    """ Form for adding a new cupcake to the databse, through the API. """

    flavor = StringField(
        "Flavor: ",
        validators=[InputRequired()]
    )

    size = SelectField(
        "Size: ",
        choices=[
            ('small', 'Small'), 
            ('medium', 'Medium'), 
            ('large', 'Large'), 
        ],
        validators=[InputRequired()]
    )

    rating = SelectField(
        "Rating: ",
        choices=[
            ('1', '1'), 
            ('2', '2'), 
            ('3', '3'), 
            ('4', '4'), 
            ('5', '5'), 
            ('6', '6'), 
            ('7', '7'), 
            ('8', '8'), 
            ('9', '9'), 
            ('10', '10'), 
        ],
        validators=[InputRequired()]
    )

    image = StringField(
        "Image URL (optional): ",
        validators=[URL(), Optional()]
    )