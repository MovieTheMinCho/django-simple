from django.urls import path
from .views import ResiterView, LoginView

urlpatterns = [
  path('register/', ResiterView.as_view()),
  path('login/', LoginView.as_view())
]