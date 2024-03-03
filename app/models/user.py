from .. import db
from datetime import datetime
from . import CUID, CUID_LENGTH, UTC_TIME

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.String(CUID_LENGTH), primary_key=True, default=CUID.generate())
  name = db.Column(db.String(50))
  email = db.Column(db.String(75), unique=True)
  password = db.Column(db.Text)
  email_verified = db.Column(db.Boolean, default=False)
  image = db.Column(db.Text)
  created_at = db.Column(db.DateTime, default=datetime.now(UTC_TIME))
  updated_at = db.Column(db.DateTime, default=datetime.now(UTC_TIME), onupdate=datetime.now(UTC_TIME))
  deleted_at = db.Column(db.DateTime, nullable=True)
  
  def __init__(self, name, email, password, email_verified=None, image=None):
    self.name = name
    self.email = email
    self.password = password
    self.email_verified = email_verified
    self.image = image
    
  def __repr__(self):
    return '<id {}>'.format(self.id)
  
  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'password': self.password,
      'email_verified': self.email_verified,
      'image': self.image,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }