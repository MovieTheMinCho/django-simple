from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from account.models import GeneralUser
from .models import Article
from .serializer import ArticleSerizliser

# Create your views here.

class ArticleView(ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerizliser

  @method_decorator(login_required)
  def create(self, request, *args, **kwargs):
    pk = request.session.get('_auth_user_id')
    if pk == None:
      return Response({"result":"Please Login"})
    author = GeneralUser.objects.get(pk=pk)
    article = Article(
      author=author, 
      title=request.data['title'], 
      content=request.data['content'])
    article.save()
    return Response(status=200)