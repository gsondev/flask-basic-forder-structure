from ...routes import welcome_route

def test_welcome():
  assert welcome_route.welcome() == "Welcome to the API"