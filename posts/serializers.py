from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerilaizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']


class PostSerilaizers(serializers.ModelSerializer):
    author=UserSerilaizers()
    category=serializers.StringRelatedField()
    class Meta:
        model=Post              #form for model(Post)
        fields='__all__'         #all columns  appear in form 
        
