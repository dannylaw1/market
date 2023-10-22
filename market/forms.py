from flask_wtf import FlaskForm 
from  wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length, EqualTo,Email,ValidationError
from market.models import User
from market.models import User


 
class RegisterFrom(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('The email address you provided already exists! Please try a different email.')

    username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password:', validators=[DataRequired(), Length(min=2), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField(' Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PurchaseItemForm(FlaskForm):
    submit=SubmitField("Purchase Item")



class PaymentItemForm(FlaskForm):
    submit=SubmitField("Done")


class SellItemForm(FlaskForm):
    submit=SubmitField("Remove Item !")