from . import base_api

@base_api.route('/', methods=['GET'])
def welcome():
  return 'Welcome to the API'