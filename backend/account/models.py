from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created = models.DateField(auto_now_add=True)
  introduction = models.CharField(max_length=1500, blank=True)

  def __str__(self):
    return self.user.__str__()