from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

#To validate New user sign in 
class RegistrationForms(FlaskForm): 
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()]) 
    password=PasswordField(
        "Password",
        validators=[
            DataRequired(), 
            Length(min=8, message="Password must be 8 characters long")
        ]
    )
    confirm_password=PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password",message="Passwords Must Match.")
        ]
    )
    submit = SubmitField("Sign Up") 

#To validate Login from users
class LoginForm(FlaskForm): 
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()]) 
    submit = SubmitField("Login")