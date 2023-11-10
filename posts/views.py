from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):

    data=Post.objects.all( )  #from db get all posts

    context={
        'khawlah':data
    }
    return render(request,'posts/post_list.html',context)


def post_details(request,post_id):
    data=Post.objects.get(id=post_id)
    context={
        'post_de':data
    }
    return render(request,'posts/post_details.html',context)




""" 
def post_list(request):

    data=Post.objects.all( )  #query
    context={'khawlah':data}  #context
    return render(request,'posts/post_list.html',context) #templeate
 """


from django.views.generic import ListView
class PostList(ListView):             #context_list object_list
    model=Post
