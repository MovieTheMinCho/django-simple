from rest_framework import serializers

from .models import Article

class ArticleSerizliser(serializers.ModelSerializer):
  class Meta:
    model = Article
    field = ['id', 'title', 'content', 'author', 'created']