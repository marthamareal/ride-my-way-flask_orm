from database import db, BaseModel
class User(db.Model, BaseModel):

    __tablename__ = 'users'

    username = db.Column(db.String())

    def __repr__(self):
        return f'<User self.username>'