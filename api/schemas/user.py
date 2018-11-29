from marshmallow import fields, post_load

from api import ValidationError
from api.models import User
from .base_schema import BaseSchema
from ..messages import serialization_errors
from ..utilities import validate_email, validate_password, validate_username


class UserSchema(BaseSchema):

    username = fields.String(
        required=True,
        error_messages={'required': serialization_errors['feild_required']},
        validate= validate_username
    )

    email = fields.String(
        required=True,
        error_messages={'required': serialization_errors['feild_required']},
        validate=validate_email
    )

    password = fields.String(
        required=True,
        load_only=True,
        error_messages={'required': serialization_errors['feild_required']},
        validate=validate_password
    )

    @post_load
    def validate_email_or_username_exists(self, data):

        if User.query.filter_by(email=data['email']).first():
            raise ValidationError({'error': 'User with this email already exists'}, 400)

        if User.query.filter_by(username=data['username']).first():
            raise ValidationError({'error': 'User with this username already exists'}, 400)


class UpdateUserSchema(BaseSchema):

    username = fields.String(
        required=False,
        validate=validate_username
    )

    email = fields.String(
        required=False,
        validate=validate_email
    )

    password = fields.String(
        required=False,
        load_only=True,
        validate=validate_password
    )

    @post_load
    def validate_email_or_username_exists(self, data):
        """ Validate to make sure user does not use an email or username of another person when updating details"""

        pass
