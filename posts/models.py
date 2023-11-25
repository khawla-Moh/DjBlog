from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

'''
   post:
       -title
       -content
       -draft
       -publish_date
       -author
       -image
       -tags
       -category
       -comments

'''

class Post(models.Model):
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=20000)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)    
    tags = TaggableManager() 
    image=models.ImageField(upload_to='post')
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True)
    """ publish_date2=models.DateTimeField(auto_now=True)
     """
    
    def __str__(self):
        return self.title 
    
class Category(models.Model):
    name=models.CharField(max_length=100) 

    def __str__(self):
        return self.name   
    
class Comments(models.Model):
    post=models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    Comments=models.TextField(max_length=500)
    created_at=models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return str(self.post)