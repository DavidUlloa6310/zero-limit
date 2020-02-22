from datetime import datetime
from zero_limit import db

class customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    parent_name = db.Column(db.String(), unique = False, nullable = False)
    child_name = db.Column(db.String(), unique = True, nullable = False)
    email = db.Column(db.String(), unique = False, nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location_name = db.Column(db.String(), db.ForeignKey('location.name'))

    def __repr__(self):
        return f"Customer({self.id}): {self.parent_name}, Child: {self.child_name}, Email: {self.email} @ {self.date_created.month}/{self.date_created.day}/{self.date_created.year}"

class location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = False, nullable = False)
    address = db.Column(db.String(), unique = True, nullable = False)
    max_reservations = db.Column(db.Integer, nullable = False)
    current_reservations = db.Column(db.Integer, default = 0)
    logo = db.Column(db.String(20), nullable = False, default='location_icons\default.jpg')
    customers = db.relationship('customer', backref='location')

    def add_reservation(self):
        self.current_reservations += 1

    def check_availability(self):
        return self.current_reservations < self.max_reservations
    
    def __repr__(self):
        return f"Location({self.id}): {self.name}, Address: {self.address}, Max Reservations: {self.max_reservations}, Current Reservations: {self.current_reservations}"