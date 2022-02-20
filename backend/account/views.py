from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
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
    logined_user = request.session.get('user', 'unlogin')
    return Response({'user':logined_user}, status=status.HTTP_200_OK)

  def post(self, request):
      serializer = self.serializer_class(
        data=request.data, 
        context={'request':request})
      rst = serializer.is_valid(raise_exception=True)
      username = serializer.validated_data['user'].username
      if rst:
        request.session['login'] = username
      return Response({'sucess': rst, 'user':username}, status=status.HTTP_200_OK)

    