from .database import db, ModelOperations


class User(db.Model, ModelOperations):

    __tablename__ = 'users'

    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<User self.username>'
