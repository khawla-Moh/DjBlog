from django.db import models
from taggit.managers import TaggableManager

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
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=20000)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField()    
    tags = TaggableManager() 
    image=models.ImageField(upload_to='post')
    """ publish_date2=models.DateTimeField(auto_now=True)
     """
    
    def __str__(self):
        return self.title 