from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField() 
    status =  models.BooleanField(default = True)

class Category(models.Model):
    title = models.CharField(max_length=50)
    status =  models.BooleanField(default = True)

class Talent(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default = True)

class Blog(models.Model):
    image = models.ImageField(upload_to='blog',default= 'family.jpeg' )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talent = models.ManyToManyField(Talent)
    category = models.ManyToManyField(Category)
    insta_id = models.CharField(max_length=50)
    feedbook_id = models.CharField(max_length=50) 
    comments = models.ManyToManyField(Comments)
    name = models.CharField(max_length=50)
    content = models.TextField()
