from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.fields.html5 import TelField
from wtforms.validators import InputRequired

from data import goals


class ClientForm(FlaskForm):
    name = StringField('Вас зовут', [InputRequired(message='Это поле не может быть пустым.')])
    phone = TelField('Ваш телефон', [InputRequired(message='Это поле не может быть пустым.')])
    submit = SubmitField()


class BookingForm(ClientForm):
    day = HiddenField()
    time = HiddenField()
    profile_id = HiddenField()


class RequestForm(ClientForm):
    goal = RadioField('goal', choices=list(goals.items()), validators=[InputRequired()])
    time = RadioField('time', choices=[(value, value) for value in ('1-2', '3-5', '5-7', '7-10')],
                      validators=[InputRequired()])
