from django.shortcuts import render,redirect
from .models import Post,Comments
from .forms import PostForm,CommentsForm

# Create your views here.


def post_list(request):
    data=Post.objects.all( )  #from db get all posts
    context={
        'khawlah':data
    }
    return render(request,'posts/post_list.html',context)


def post_details(request,post_id):
    data=Post.objects.get(id=post_id)
    comments=Comments.objects.filter(post=data)          #to display comments in post #post >>coulmn in comment
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=data
            myform.save()
    else:
        form=CommentsForm()

    context={
        'post_de':data,
        'comments':comments ,                            #dispaly comments in html    
         'form':form
    }
    return render(request,'posts/post_details.html',context)


def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myfrom= form.save(commit=False)
            myfrom.author=request.user
            myfrom.save()
            return redirect('/posts/')
    else:
        form=PostForm    
    return render(request,'posts/new.html',{'form':form})


def edit_post(request,pk):
    post=Post.objects.get(id=pk)    
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myfrom= form.save(commit=False)
            myfrom.author=request.user
            myfrom.save()
            return redirect('/posts/')
    else:
        form=PostForm(instance=post)
    return render(request,'posts/edit.html',{'form':form})



def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')



""" 
def post_list(request):

    data=Post.objects.all( )  #query
    context={'khawlah':data}  #context
    return render(request,'posts/post_list.html',context) #templeate
 """

