from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  introduction = models.CharField(max_length=1500, blank=True)

  def __str__(self):
    return self.user.username

  class Meta:
    verbose_name = "Profile"
    verbose_name_plural = "Profiles"
  