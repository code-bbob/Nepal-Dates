from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    description = models.CharField(max_length = 100)
    sex = models.BooleanField()
    age = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class ProfileImages(models.Model):
    profile = models.ForeignKey(Profile, related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/images')