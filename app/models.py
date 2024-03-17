from . import db
from flask import url_for
from flask import current_app
#from werkzeug.security import generate_password_hash


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of Property would create a
    # property (singular) table, but if we specify __tablename__ we can change it
    # to `[properties] (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(400))
    description = db.Column(db.String(800))
    no_of_rooms = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(150))
    image_filename = db.Column(db.String(255), nullable=True)


    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
        
    def get_photo_url(self):
        return current_app.config['UPLOAD_FOLDER'] + '/' + self.image_filename
    
    def get_image_filename(self):
        return self.image_filename
    

    def __repr__(self):
        #return '<User %r>' % (self.username)
        return f"<Property {self.property_title}>"
    
    
    def __init__(self, property_title, description , no_of_rooms, no_of_bathrooms, price, property_type, location, image_filename):
        self.property_title = property_title
        self.description = description 
        self.no_of_rooms = no_of_rooms
        self.no_of_bathrooms = no_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.image_filename = image_filename

