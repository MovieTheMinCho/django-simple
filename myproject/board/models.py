from django.db import models

# Create your models here.

class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1500)
    author = models.CharField(max_length=10)
    id_number = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.title
