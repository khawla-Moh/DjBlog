from django import forms
from .models import Post,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model=Post              #form for model(Post)
        # fields='__all__'         #all columns  appear in form 
        exclude=('author',)

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['user','Comments']       
        #fields='__all__'       