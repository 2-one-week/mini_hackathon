from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=500, blank=False)
    location = models.CharField(max_length=30, blank=False)
    hidden_loc = models.CharField(max_length = 20, blank=False, null=True)
    trust = models.CharField(max_length = 10, null=True)
    
# class 
    
