from django.db import models
from accounts.models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class SpecialServices(models.Model):
    title = models.CharField(max_length=50) 
    content = models.TextField()
    status = models.BooleanField(default = True)

class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50) 
    content = models.TextField()
    status = models.BooleanField(default = True)


class skill(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default = True)


class TeamMain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    skill = models.ManyToManyField(skill)
    image = models.ImageField(upload_to='team',default= 'family.jpeg')
    insta_id = models.CharField(max_length=50)
    feedbook_id = models.CharField(max_length=50) 
    status = models.BooleanField(default = True)
