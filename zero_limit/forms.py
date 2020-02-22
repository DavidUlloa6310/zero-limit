from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class reservation_form(FlaskForm):
    parent_name = StringField('Parent Name', validators=[DataRequired()])
    child_name = StringField('Child Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
