from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    description = models.CharField(max_length = 100)
    Sex = models.BooleanField()
    age = models.IntegerField()
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="profiles/images")
    