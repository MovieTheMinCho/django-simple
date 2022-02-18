from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length=1500)
    created = models.DateField(auto_now=True)

    class Meta:
        ordering=['created']

