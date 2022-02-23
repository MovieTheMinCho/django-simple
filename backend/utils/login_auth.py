from rest_framework.response import Response
from rest_framework import status

def login_auth_deco_with_method(lookup):
  def wrapper(func):
    def inner(*args, **kwargs):
      request = args[1]
      user_id = get_auth_user_id(request)
      if kwargs.get(lookup) != int(user_id):
        return Response(status.HTTP_401_UNAUTHORIZED)
      return func(*args, **kwargs)
    return inner
  return wrapper

def get_auth_user_id(request):
  return request.session.get('_auth_user_id')