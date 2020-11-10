from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app): 
    db.app = app
    db.init_app(app)

class Pet(db.Model): 
    """pet model"""

    __tablename__ = 'pets'

    def __repr__(self): 
        p = self
        return f"<pet_id = {p.id}, name = {p.name}, species = {p.species}, is_available = {p.is_available}"

    id = db.Column(db.Integer, 
                    primary_key = True, 
                    autoincrement = True)

    name = db.Column(db.String, 
                        nullable = False)

    species = db.Column(db.String, 
                        nullable = False)
    
    photo_url = db.Column(db.String, 
                        nullable = True, 
                        unique = True)

    age = db.Column(db.Integer, 
                        nullable = True)

    
    notes = db.Column(db.Text, 
                        nullable = True)
    
    is_available = db.Column(db.Boolean, 
                            nullable = False,
                            default=True)
