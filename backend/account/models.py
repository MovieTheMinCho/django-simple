from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  introduction = models.CharField(max_length=1500, blank=True)

  def __str__(self):
    return self.user.username
  
  def to_json(self):
    user = self.user
    username = user.username
    email = user.email
    introduction = self.introduction
    date_joined = self.user.date_joined
    ret = {
      'username':username,
      'email':email,
      'introduction': introduction,
      'date_joined': date_joined
    }
    return ret