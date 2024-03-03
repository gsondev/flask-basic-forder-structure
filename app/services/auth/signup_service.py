from ...models.user import User
from ... import db
import bcrypt
from flask import jsonify
from ...utils.logger import Logger
import traceback

class SignupService:
  def __init__(self, name, email, password, email_verified=None, image=None):
    self.name = name
    self.email = email
    self.password = password
    self.email_verified = email_verified
    self.image = image

  def signup(self):
    try:
      user = User.query.filter_by(email=self.email).first()
      if user:
        return jsonify({'message': 'User already exists'}), 400
      else:
        hasehd_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(
          name=self.name,
          email=self.email,
          password=hasehd_password,
          email_verified=self.email_verified,
          image=self.image
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
      Logger.add_to_log('error', str(e))
      Logger.add_to_log('error', traceback.format_exc())
      return jsonify({'message': str(e), 'error': True }), 500