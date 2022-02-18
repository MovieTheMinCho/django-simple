from django.urls import path
from . import views

urlpatterns = [
        path('', views.ArticleView.as_view(
            {'get':'list',
            'post':'create'}
            )),
        path('<int:pk>', views.ArticleView.as_view(
            {'get':'retrieve'}
            )),
        ]
