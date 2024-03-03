from ...models.user import User
from ... import db
import bcrypt
from flask import jsonify
from ...utils.logger import Logger
import traceback

def SigninService(email, password):
  try:
    user = User.query.filter_by(email=email).first()
    if user:
      if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'message': 'User logged in successfully'}), 200
      else:
        return jsonify({'message': 'Incorrect password'}), 400
    else:
      return jsonify({'message': 'User not found'}), 404
  except Exception as e:
    Logger.add_to_log('error', str(e))
    Logger.add_to_log('error', traceback.format_exc())
    return jsonify({'message': str(e), 'error': True }), 500