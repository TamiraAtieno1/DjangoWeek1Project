from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog2(models.Model):
    image = models.ImageField(blank=True, upload_to="images", default= 'images/Ireland.jpg')
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    text = models.TextField(default='None')

    def __str__(self):
        return self.title