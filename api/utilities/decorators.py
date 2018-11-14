""" 
    This file contains all decorators that are used by the application.

    Decorators are built usin a wrap function  
"""
from flask import request
# Third party imports
from functools import wraps
from .base_validator import ValidationError


def validate_json_data(func):
    """
        Validates the user input if its a json formart

        Args:
           func(function): Function to be called when conditions are met
        Returns:
            The decorated function
        Raises:
            ValidationError: Incase input data is not a json format     
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        if request.is_json:
            return func(*args, **kwargs)
        raise ValidationError({'message':'Please provide a valid Json data format'}, 400)  

    return decorated

