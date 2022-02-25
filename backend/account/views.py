from django.contrib.auth import login, logout, get_user_model, authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, mixins
from utils.login_auth import login_auth_deco_with_method

from .models import Profile

from .serializer import LoginSerializer, ProfileSerializer

User = get_user_model()

# Create your views here.

class LoginView(GenericAPIView):
  serializer_class = LoginSerializer

  def get(self, request):
    return Response({'session':request.session}, status=status.HTTP_200_OK)

  def post(self, request):
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return Response({'user':username, 'status':"logined"}, status=status.HTTP_200_OK)
      else:
        return Response({'user':username, 'status':"can't find user"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
  def get(self, request):
    logout(request)
    return Response({'session':request.session}, status=status.HTTP_200_OK)

class ProfileView(
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  GenericViewSet):
  serializer_class = ProfileSerializer
  queryset = Profile.objects.all()
  lookup_field='pk'

  @login_auth_deco_with_method(lookup_field)
  def destroy(self, request, *args, **kwargs):
    return super().destroy(request, *args, **kwargs)
  
  @login_auth_deco_with_method(lookup_field)
  def partial_update(self, request, *args, **kwargs):
    user = Profile.objects.get(pk=kwargs.get('pk'))
    serializer = self.get_serializer(user, request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(status.HTTP_400_BAD_REQUEST)
