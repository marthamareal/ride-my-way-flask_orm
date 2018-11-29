from flask_restplus import Resource
from flask import request

from api.schemas.user import UpdateUserSchema
from .. import api
from ..utilities.decorators import validate_json_data
from ..schemas import UserSchema
from ..models import User
from  ..utilities.messages.success_messages import SUCCESS_MESSAGES

USER_SCHEMA = UserSchema()


@api.route('/users')
class UserResource(Resource):

    """ Resource class for creating users and getting list of users"""

    @validate_json_data
    def post(self):

        request_data = request.get_json()

        user_data = USER_SCHEMA.load_object_into_schema(request_data, partial=False)
        User(**user_data).save()
        return {
                   'data': user_data,
                   'message': SUCCESS_MESSAGES['created'].format('User'),
                   'status': 'success'
                   }, 201

    def get(self):

        users = UserSchema(many=True).dump(User.query.all()).data

        return {
                   'data': users,
                   'message': SUCCESS_MESSAGES['fetched'].format('Users'),
                   'status': 'success'
               }, 200


@api.route('/users/<string:user_id>')
class SingleUserResource(Resource):

    """ Resource class for creating users and getting list of users"""

    @validate_json_data
    def patch(self, user_id):

        request_data = request.get_json()
        user = User.get_or_404(user_id)
        new_user_data = UpdateUserSchema().load_object_into_schema(request_data)
        user.update(**new_user_data)

        return {
                   'data': USER_SCHEMA.dump(user).data,
                   'message': SUCCESS_MESSAGES['updated'].format('User'),
                   'status': 'success'
                   }, 200

    def delete(self, user_id):

        user = User.get_or_404(user_id)
        user.delete()

        return {
                   'message': SUCCESS_MESSAGES['deleted'].format('User'),
                   'status': 'success'
               }, 200

    def get(self, user_id):
        user = User.get_or_404(user_id)

        return {
                   'data': USER_SCHEMA.dump(user).data,
                   'message': SUCCESS_MESSAGES['fetched'].format('User'),
                   'status': 'success'
               }, 200
