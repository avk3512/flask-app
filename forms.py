from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from db import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

    # def validate_username(self, username):
    #     user = User.query.filter_by(nickname=username.data).first()
    #     if user is None:
    #         raise ValidationError('Invalid username or password')
    #
    # def validate_password(self, password):
    #     user = User.query.filter_by(nickname=self.username.data).first()
    #     if user is None or not user.check_password(password.data):
    #         raise ValidationError('Invalid username or password')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    # def validate_username(self, username):
    #     user = User.query.filter_by(nickname=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')
    #
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')
