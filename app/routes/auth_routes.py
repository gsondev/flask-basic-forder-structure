from . import base_api
from flask import request, jsonify
from ..utils.logger import Logger
import traceback
from ..services.auth.signup_service import SignupService
from ..services.auth.signin_service import SigninService

@base_api.route('/signup', methods=['POST'])
def signup():
  try:
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    # campos no obligatorios
    verify_password = data.get('verify_password', None)
    image = data.get('image', None)
    return SignupService(name, email, password, verify_password, image).signup()
  except Exception as e:
    Logger.add_to_log('error', str(e))
    Logger.add_to_log('error', traceback.format_exc())
    return jsonify({'message': str(e), 'error': True})

@base_api.route('/signin', methods=['POST'])
def signin():
  try:
    data = request.get_json()
    email = data['email']
    password = data['password']
    return SigninService(email, password)
  except Exception as e:
    Logger.add_to_log('error', str(e))
    Logger.add_to_log('error', traceback.format_exc())
    return jsonify({'message': str(e), 'error': True})