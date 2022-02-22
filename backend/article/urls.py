from django.urls import path

from .views import ArticleView

urlpatterns = [
  path('', ArticleView.as_view({'get':'list', 'post':'create'})),
  path('<int:pk>/', ArticleView.as_view({'get':'retrieve'})),
]