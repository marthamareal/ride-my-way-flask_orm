from flask_restplus import Resource
from flask import request
from .. import api
from ..utilities.decorators import validate_json_data

@api.route('/users')
class UserResource(Resource):

    """ Resource class for creating users and getting list of users"""

    @validate_json_data
    def post(self):
        
        return request.get_json()

    def get(self):
        return