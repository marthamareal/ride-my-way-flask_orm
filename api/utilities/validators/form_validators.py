import re

from marshmallow import ValidationError as MarshValidationError


def validate_email(data):
    email_regex = "^[a-zA-Z0-9]+(.[a-zA-Z0-9]+)*@[a-z].[a-z]{2,4}"

    if not re.match(email_regex, data):
        raise MarshValidationError('Invalid email, please provide an email with a valid format')


def validate_password(data):
    password_regex = "^[a-zA-Z0-9_@*%]{8,}"

    if not re.match(password_regex, data):
        raise MarshValidationError('Password should have 8 or more characters')


def validate_username(data):
    username_regex = "^[a-zA-Z0-9]{5,}"

    if not re.match(username_regex, data):
        raise MarshValidationError('Username should have 5 or more characters')
