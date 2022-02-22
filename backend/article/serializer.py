from rest_framework import serializers
from django.contrib.auth.models import User

from account.models import GeneralUser

from .models import Article

class UserSerialzier(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username']

class AuthorSerializer(serializers.ModelSerializer):
  user = UserSerialzier(read_only=True)
  class Meta:
    model = GeneralUser
    exclude = ['introduction']
    depth=3

class ArticleSerizliser(serializers.ModelSerializer):
  author = AuthorSerializer(read_only=True)

  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ['id', 'created']
    depth = 3