from django.urls import path

from .views import ArticleView, CommentView

urlpatterns = [
  path('', ArticleView.as_view({
    'get':'list', 
    'post':'create'})), 
  path('<int:pk>/', ArticleView.as_view({
    'get':'retrieve', 
    'delete':'destroy'})),
  path('<int:pk>/comment/', CommentView.as_view({
    'get':'list', 
    'post':'create'})),
  path('<int:pk>/comment/<int:cpk>', CommentView.as_view({
    'get':'retrieve',
    'delete':'destroy'
  }))
]