from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Pet """

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(30),
                     nullable=False)
    
    species = db.Column(db.String(30),
                     nullable=False)

    photo_url = db.Column(db.String(20000))

    age = db.Column(db.Integer)

    notes = db.Column(db.String(500))

    available = db.Column(db.Boolean,
                    default=True,
                    nullable=False)
    
    def __repr__(self):
        return f'<Pet {self.name} {self.species} {self.age} {self.available}>'