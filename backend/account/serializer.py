from rest_framework import serializers
from .models import GeneralUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ResiterSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=10)
  email = serializers.EmailField(required=False)
  introduction = serializers.CharField(max_length=1500, required=False)
  password = serializers.CharField(style={"input_type":"password"})
  ck_password = serializers.CharField(style={"input_type":"password"})

  def validate(self, attrs):
    password = attrs.get('password')
    ck_password = attrs.get('ck_password')
    username = attrs.get('username')
    if User.objects.filter(username=username).first():
      raise serializers.ValidationError("The username has been used.")
    if password != ck_password:
      raise serializers.ValidationError("The both passwords are different.")
    return attrs

  def create(self, validated_data):
    userinfo = {}
    userinfo['username'] = validated_data.get('username')
    userinfo['password'] = validated_data.get('password')
    if validated_data.get('email'):
      userinfo['email'] = validated_data.get('email')
    generalUser = {}
    generalUser['user'] = User.objects.create_user(**userinfo)
    if validated_data.get('introduction'):
      generalUser['introduction'] = validated_data.get('introduction')
    user = GeneralUser.objects.create(
      **generalUser
    )
    user.save()
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=10)
  password = serializers.CharField(style={"input_type":"password"})

  def validate(self, attrs):
    username = attrs.get('username')
    password = attrs.get('password')
    try:
      user = User.objects.get(username=username)
    except:
      raise serializers.ValidationError("The id is incorrect.")
    print(user.password)
    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
      raise serializers.ValidationError("The password is incorrect.")
    attrs['user'] = user
    return attrs