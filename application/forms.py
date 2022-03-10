from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import Length, NumberRange, InputRequired, Regexp
from application.models import Reviews, Restaurants



class AddReviews(FlaskForm): #man
    title = StringField("review title", validators=[InputRequired()])
    review = StringField("review body", validators=[InputRequired()])
    rating = IntegerField('Rating (1-10)',validators=[InputRequired(),NumberRange(min=1, max=10)])
    restaurants_ID = SelectField('Restaurant to review', choices=[])
    submit = SubmitField('Submit your review!')

class AddRestaurants(FlaskForm):
    name = StringField("restaurant name", validators=[InputRequired()])
    cuisine = StringField("restaurant cuisine", validators=[InputRequired()])
    submit = SubmitField('Save Restaurant')


    

