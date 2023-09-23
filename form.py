from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
  name = StringField('Full Name', validators=[DataRequired(), Length(min=4)])
  surname = StringField('Full Surname', validators=[DataRequired(), Length(min=4)])
  email = StringField('Email', validators=[DataRequired(), Email(), Length(min=4)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
  confirmation_password = PasswordField('Password again', validators=[DataRequired(), EqualTo('password')])