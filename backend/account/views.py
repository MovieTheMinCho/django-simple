from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from account.models import GeneralUser
from .serializer import ResiterSerializer, LoginSerializer

# Create your views here.

class ResiterView(CreateAPIView):
  serializer_class = ResiterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    rst = serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'success':rst}, status=status.HTTP_200_OK)

class LoginView(GenericAPIView):
  serializer_class = LoginSerializer

  def get(self, request):
    return Response({'session':request.session}, status=status.HTTP_200_OK)

  def post(self, request):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return Response({'user':username, 'status':"logined"}, status=status.HTTP_200_OK)
      else:
        return Response({'user':username, 'status':"can't find user"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(GenericAPIView):
  def get(self, request):
    logout(request)
    return Response({'session':request.session}, status=status.HTTP_200_OK)

class Profile(GenericAPIView):
  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk', None)
    if pk == None:
      pk = request.session.get('_auth_user_id')
      user = GeneralUser.objects.get(pk=pk)
    else:
      user = GeneralUser.objects.get(pk=kwargs['pk'])
    return Response({'user':user.to_json()}, status=status.HTTP_200_OK)
