from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, get_hasher

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  ckeck_password = serializers.CharField(write_only=True, style={'input_type':'password'})
  def __init__(self, instance=None, data=..., **kwargs):
      self.salt = get_hasher().salt()
      super().__init__(instance, data, **kwargs)

  def validate_ckeck_password(self, value):
    return make_password(value, salt=self.salt)

  def validate_password(self, value):
    return make_password(value, salt=self.salt)

  def validate(self, attrs):
    password = attrs.get('password')
    ck_password = attrs.get('ckeck_password')
    print(password, ck_password, sep='\n')
    if password != ck_password:
      raise serializers.ValidationError("The both passwords are different.")
    return attrs

  class Meta:
    model=User
    fields=['username', 'password', 'ckeck_password', 'first_name', 'last_name', 'email']
    extra_kwargs = {
      'password': {
        'write_only': True,
        'style': {
          'input_type':'password'
          }
        }
      }

class ProfileSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  def create(self, validated_data):
    user_data = validated_data.pop('user')
    user_data.pop('ckeck_password')
    user = User.objects.create(**user_data)
    profile = Profile.objects.create(user=user, **validated_data)
    return profile

  def update(self, instance, validated_data):
    user_data = validated_data.pop('user')
    user = instance.user

    instance.introduction = validated_data.get('introduction', instance.introduction)
    instance.save()

    user.username = user_data.get('username', user.username)
    user.email = user_data.get('email', user.email)
    user.first_name = user_data.get('first_name', user.first_name)
    user.last_name = user_data.get('last_name', user.last_name)
    user.save()

    return instance

  class Meta:
    model=Profile
    fields="__all__"
    depth=2 

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=10)
  password = serializers.CharField(style={"input_type":"password"})
