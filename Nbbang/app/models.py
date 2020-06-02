from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=500, blank=False)
    location = models.CharField(max_length=30, blank=False)
    hidden_loc = models.CharField(max_length = 20, blank=False, null=True)
    trust = models.CharField(max_length = 10, null=True)
    money = models.CharField(max_length = 100, null=True)
    
    def __str__(self):
        return self.nickname
        
    
class food(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='food_id', null=True )
    title = models.CharField(max_length= 100, help_text='최대 100자 내로 입력가능합니다.')
    location = models.CharField(max_length = 50, null=True)
    deadline1 = models.CharField(max_length = 20)
    deadline2 = models.CharField(max_length = 20)
    appLink = models.CharField(max_length = 100)
    left = models.CharField(max_length = 100)
    baedalTip = models.CharField(max_length = 100)
    kakaolLnk = models.CharField(max_length = 100)
    memo = models.TextField(null= True)
    end = models.CharField(max_length = 10, null= True)
    
    def __str__(self):
        return self.title

class ott(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='ott_id', null=True )
    title = models.CharField(max_length= 100, help_text='최대 100자 내로 입력가능합니다.')
    people = models.CharField(max_length = 10)
    appLink = models.CharField(max_length = 100)
    memo = models.TextField(null= True)
    end = models.CharField(max_length = 10, null= True)
    
    def __str__(self):
        return self.title
    
class shopping(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='shopping_id', null=True )
    title = models.CharField(max_length= 100, help_text='최대 100자 내로 입력가능합니다.')
    deadline1 = models.CharField(max_length = 20)
    deadline2 = models.CharField(max_length = 20)
    siteLink = models.CharField(max_length = 100)
    left = models.CharField(max_length = 100)
    end = models.CharField(max_length = 10, null= True)
    
    def __str__(self):
        return self.title

class franchise(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='franchise_id', null=True )
    title = models.CharField(max_length= 100, help_text='최대 100자 내로 입력가능합니다.')
    deadline1 = models.CharField(max_length = 20)
    deadline2 = models.CharField(max_length = 20)
    shop = models.CharField(max_length = 50)
    item = models.CharField(max_length = 50)
    event = models.CharField(max_length = 50)
    kakaolLnk = models.CharField(max_length = 100)
    memo = models.TextField(null= True)
    end = models.CharField(max_length = 10, null= True)
    
    def __str__(self):
        return self.title

class others(models.Model):
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='others_id', null=True )
    title = models.CharField(max_length= 100, help_text='최대 100자 내로 입력가능합니다.')
    deadline1 = models.CharField(max_length = 20)
    deadline2 = models.CharField(max_length = 20)
    siteLink = models.CharField(max_length = 100)
    kakaolLink = models.CharField(max_length = 100)
    memo = models.TextField(null= True)
    end = models.CharField(max_length = 10, null= True)
    
    def __str__(self):
        return self.title