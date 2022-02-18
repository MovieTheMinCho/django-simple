from rest_framework import serializers
from .models import Article
from datetime import datetime

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length = 1500)
    created = serializers.DateField(required=False)
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        article = Article(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.created = datetime.now()
        intance.save()
        return instance

    class Meta:
        model = Article
        field = ('title', 'content')
