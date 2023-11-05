from django.db import models

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