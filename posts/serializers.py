from rest_framework import serializers
from .models import Post




class PostSerilaizers(serializers.ModelSerializer):
    class Meta:
        model=Post              #form for model(Post)
        fields='__all__'         #all columns  appear in form 
        
