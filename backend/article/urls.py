from django.urls import path

from .views import ArticleView, CommentView

urlpatterns = [
  path('', ArticleView.as_view({
    'get':'list', 
    'post':'create'})), 
  path('<int:pk>/', ArticleView.as_view({
    'get':'retrieve', 
    'delete':'destroy'})),
  path('<int:article_id>/comment/', CommentView.as_view({
    'get':'list', 
    'post':'create'})),
  path('<int:article_id>/comment/<int:comment_id>', CommentView.as_view({
    'get':'retrieve',
    'delete':'destroy'
  }))
]