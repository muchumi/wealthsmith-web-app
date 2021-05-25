from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from models.clients import Clients

# a client registration form
class ClientsRegistrationForm(FlaskForm):
    firstName = StringField('First Name', validators = [DataRequired(), Length(min = 4, max = 20)])
    lastName = StringField('Last Name', validators= [DataRequired(), Length(min = 4, max = 20)])
    username = StringField('Username', validators= [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email(), Length(min = 5, max = 100)])
    mobile_number = IntegerField('Mobile Number', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', 'confirm password must be equal to password you typed in before, please try again!')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

     # The below method validates the client input username  to avoid duplication of username in the database

    def validate_username(self, username):
        client = Clients.query.filter_by(username=username.data).first()
        if client:
            raise ValidationError('That username is taken,please choose a different one')

    # The below method validates the client input email to avoid duplication of emails in the database
    def validate_email(self, email):
        client = Clients.query.filter_by(email=email.data).first()
        if client:
            raise ValidationError('That email is taken,please choose a different one')

