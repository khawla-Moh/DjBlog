from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post              #form for model(Post)
        # fields='__all__'         #all columns  appear in form 
        exclude=('author',)