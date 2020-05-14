from django.db import models

# Create your models here.

class Reviews(models.Model):
    stars = models.IntegerField()
    comments = models.CharField(max_length=300)