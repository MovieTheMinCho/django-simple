from django.urls import path

from . import views

urlpatterns = [
    path('', views.MyApiView.as_view()),
    path('<int:article_id>', views.IdApiView.as_view())
]
