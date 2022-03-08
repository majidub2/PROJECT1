from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, NumberRange, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.models import reviews,restaurants



class Addreviews(FlaskForm): #many
    title = StringField("review title", validators=[InputRequired())
    review = StringField("review body", validators=[InputRequired())
    rating = IntegerField('Rating (1-5)',validators=[InputRequired(),NumberRange(min=1, max=5)])
    restaurants_ID = SelectField('Restaurant to review', choices=[])
    submit = SubmitField('Submit your review!')

# class Addrestaraunts(FlaskForm):
#     name = StringField("restaurant name", validators=[InputRequired())
#     cuisine = StringField("restaurant cuisine", validators=[InputRequired())
#     submit = SubmitField('Enter Restaurant')

    

