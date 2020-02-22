from datetime import datetime
from zero_limit import db

class location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = False, nullable = False)
    address = db.Column(db.String(), unique = True, nullable = False)
    logo = db.Column(db.String(), nullable = False, default=r'location_icons\default.jpg')
    schedule = db.Column(db.String(), nullable = False)
    
    def __repr__(self):
        return f"Location({self.id}): {self.name}, Address: {self.address}, Schedule: {self.schedule}"