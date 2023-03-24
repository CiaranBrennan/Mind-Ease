from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired
from datetime import date

class signIn(Form):
    username = TextField('username',
        validators=[DataRequired()])

    password = PasswordField('password',
        validators=[DataRequired()])

class bookApp(Form):
    appDate = DateField('appDate',
        validators=[DataRequired()])

    appTime = TimeField('appTime',
        validators=[DataRequired()])

class editApp(Form):
    appDate = DateField('appDate',
        validators=[DataRequired()])

    appTime = TimeField('appTime',
        validators=[DataRequired()])
