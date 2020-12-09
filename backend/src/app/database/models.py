from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

class User(db.Document):

    # Define a User model

    # Identification Data
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    # User Data
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)

    date_created  = db.DateTimeField(default=datetime.datetime.utcnow)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class HubspotData(db.Document):
    #Hubspot Data
    access_token = db.StringField()
    refresh_token = db.StringField()
    expires_at = db.DateTimeField()
    expires_in = db.IntField()

class Deal(db.Document):
    dealid = db.StringField()
    dealname = db.StringField()
    dealstage = db.StringField()
    closedate = db.DateTimeField()
    amount = db.StringField()
    dealtype = db.StringField()