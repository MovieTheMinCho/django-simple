from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializer import ArticleSerializer, CommentSerializer, UserSerializer
from utils.login_auth import login_auth_deco_with_method, get_auth_user_id

# Create your views here.

User = get_user_model()

class ArticleView(
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  GenericViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  lookup_field = 'pk'

  def create(self, request, *args, **kwargs):
    user_id = get_auth_user_id(request)
    if user_id == None:
      return Response(status.HTTP_401_UNAUTHORIZED)
    data = {
      'author_id':user_id,
      'title':request.data.get('title'),
      'content':request.data.get('content')}
    articleSerializer = ArticleSerializer(data=data)
    print(articleSerializer)
    if not articleSerializer.is_valid():
      return Response(status=status.HTTP_400_BAD_REQUEST)
    articleSerializer.save()
    return Response(status=status.HTTP_201_CREATED)

  @login_auth_deco_with_method(lookup_field)
  def destroy(self, request, *args, **kwargs):
    user_id = get_auth_user_id(request)
    article_id = kwargs.get(self.lookup_field)
    author = User.objects.get(pk=user_id)
    article = Article.objects.get(pk=article_id)
    if author.id != article.author.id:
      return Response(status.HTTP_401_UNAUTHORIZED)
    article.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class CommentView(
  mixins.ListModelMixin,
  mixins.DestroyModelMixin,
  mixins.RetrieveModelMixin,
  mixins.CreateModelMixin,
  GenericViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  lookup_field = 'cpk'

  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)
    
  def create(self, request, *args, **kwargs):
    article_id = kwargs.get('pk')
    author_id = get_auth_user_id(request)
    Comment.objects.create(
      author_id=author_id,
      article_id=article_id,
      content=request.data.get('content')
    )
    return super().create(request, *args, **kwargs)

  @login_auth_deco_with_method(lookup_field)
  def destroy(self, request, *args, **kwargs):
    return super().destroy(request, *args, **kwargs)
  