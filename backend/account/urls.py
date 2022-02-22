from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import LogoutView, Profile, ResiterView, LoginView

urlpatterns = [
  path('register/', ResiterView.as_view()),
  path('login/', LoginView.as_view()),
  path('logout/', LogoutView.as_view()),
  path('profile/', login_required(Profile.as_view())),
  path('profile/<int:pk>/', Profile.as_view()),
]