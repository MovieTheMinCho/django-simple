from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializer import ArticleSerizliser

# Create your views here.

class ArticleView(ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerizliser