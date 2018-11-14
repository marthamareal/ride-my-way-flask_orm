from flask import Blueprint, jsonify

class ValidationError(Exception):

    def __init__(self, error, status_code=400):
        Exception.__init__(self)
        self.error = error
        self.error['status'] = 'error'
        self.status_code = status_code

    def to_dict(self):
        return self.error

    
