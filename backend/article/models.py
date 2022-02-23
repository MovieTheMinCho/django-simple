from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Article(models.Model):
  id = models.BigAutoField(primary_key=True)
  title = models.CharField(max_length=10)
  content = models.CharField(max_length=1500)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateField(auto_now=True)

  def __str__(self):
    return self.title.__str__()

class Comment(models.Model):
  id = models.BigAutoField(primary_key=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateField(auto_now=True)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=300)

  def __str__(self):
    return ' '.join([self.article.__str__(), '-', self.author.__str__()])