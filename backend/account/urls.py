from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import LogoutView, LoginView, ProfileView

urlpatterns = [
  path('register/', ProfileView.as_view({'post':'create'})),
  path('login/', LoginView.as_view()),
  path('logout/', LogoutView.as_view()),
  path('profile/<int:pk>/', ProfileView.as_view({
    'get':'retrieve',
    'delete':'destroy',
    'patch':'partial_update'
    })),
]