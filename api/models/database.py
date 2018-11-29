from flask_sqlalchemy import SQLAlchemy
import uuid

from api import ValidationError

db = SQLAlchemy()


class BaseModel(object):

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4())


class ModelOperations(BaseModel):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    @classmethod
    def get_or_404(cls, id):

        instance = cls.get(id)

        if not instance:
            raise ValidationError(
                {
                    'error': f'{cls.__name__} not found'
                },
                404)

        return instance

    def delete(self):
        db.session.delete(self)
        db.session.commit()
