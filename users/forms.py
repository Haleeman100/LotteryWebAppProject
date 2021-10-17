import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, ValidationError, Length, EqualTo


# function to not allow user to make use of special characters in password
def character_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):
    # check for valid email address
    email = StringField(validators=[Required(), Email()])

    # check if field is filled and if invalid characters are used
    firstname = StringField(validators=[Required(), character_check])

    # check if field is filled and if invalid characters are used
    lastname = StringField(validators=[Required(), character_check])

    # check if field is filled and if correct format is used
    phone = StringField(validators=[Required()])

    # check if field is filled and requirements are satisfied
    password = PasswordField(validators=[Required(), Length(min=6, max=12, message=
    'Password must be between 6 and 12 characters in length')])

    # check if field is filled and requirements are satisfied
    confirm_password = PasswordField(validators=[Required(), EqualTo('password', message=
    'Both password fields must be equal!')])

    # check if field is filled and requirement is satisfied
    pin_key = StringField(validators=[Required(), Length(min=32, max=32, message=
    'Pin Key must be 32 characters in length')])
    submit = SubmitField(validators=[Required(), ])

    # function to allow user to make use of special characters in password
    def validate_password(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[?@!#%^&*()<>$/{}~])')
        if not p.match(self.password.data):
            raise ValidationError("Password must contain at least 1 digit, "
            "one lowercase letter, 1 uppercase letter, and 1 special character.")

    # function to validate phone number in the form of  XXXX-XXX-XXXX
    def validate_phone(self, phone):
        p = re.compile(r'\d{4}-\d{3}-\d{4}')
        if not p.match(self.phone.data):
            raise ValidationError("Phone number must be in the form XXXX-XXX-XXXX")


class LoginForm(FlaskForm):
    email = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()
