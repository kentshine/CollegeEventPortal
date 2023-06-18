from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,DateField,TimeField,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class CreateEventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    event_date = DateField('Date',validators=[DataRequired()])
    event_time = TimeField('Time',validators=[DataRequired()])
    location = SelectField('Location', choices=[("1","Main Hall"),("2","Alumini Corner"),("3","Hall No .1"),("4","Hall No .2")] , validators=[DataRequired()])
    submit = SubmitField('Create')

