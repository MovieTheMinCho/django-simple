from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Article, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username']

class ArticleSerializer(serializers.ModelSerializer):
  author = UserSerializer(read_only=True)
  author_id = serializers.IntegerField(write_only=True)

  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ['id', 'created']
    depth=2

class CommentSerializer(serializers.ModelSerializer):
  author = UserSerializer(read_only=True)
  article = ArticleSerializer(read_only=True)
  author_id = serializers.IntegerField(write_only=True)
  article_id = serializers.IntegerField(write_only=True)
  
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ['id', 'created']
    depth=2