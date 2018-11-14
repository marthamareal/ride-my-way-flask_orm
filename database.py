from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModelOperations(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def get(self):
        return self