from django.db import models
from django.utils.timezone import now


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
    publish_date=models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.title 