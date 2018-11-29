from marshmallow import Schema, fields
from ..utilities import ValidationError


class BaseSchema(Schema):

    id = fields.String(dump_only=True, )

    def load_object_into_schema(self, data, partial=False):
        data, errors = self.load(data, partial)

        if errors:
            raise ValidationError(dict(errors=errors, message='Sorry an error occured'),400)
            
        return data
