from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    password = serializers.CharField()
    class Meta:
        model = User
        field = ( 'email', 'username', 'password')
        extra_kargss = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User(
                email=validated_data['email'],
                username=validated_data['username']
                )
        user.save()
        token = Token.objects.create(user=user)
        return token.key
