
from marshmallow import ValidationError as MarshValidationError


def validate_string_length(data):
    if len(data) < 3:
        raise MarshValidationError('length must be above 3 characters')
    return data
