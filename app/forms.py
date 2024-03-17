from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, FileField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired



class PropertyForm(FlaskForm):
    property_title = StringField('Property Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    no_of_rooms = IntegerField('Number of Rooms', validators=[InputRequired()])
    no_of_bathrooms = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[InputRequired()])
    image = FileField('Image File', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])