from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializer import UserSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class SignupView(CreateAPIView):
    queryset = User.objects.all(
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        user = authenticate(
                username=request.data.get('id'),
                password=request.data.get('password'))
        if user is not None:
            token = Token.object.get(user=user)
            return Response({"Token", token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

