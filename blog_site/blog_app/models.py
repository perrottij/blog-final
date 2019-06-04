import django.utils.timezone
from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=50)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title
