from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
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


from django.views.generic import ListView,UpdateView,CreateView,DeleteView

class PostList(ListView):             #context:model_list ,object_list
    model=Post                        #template:mode;_action=post_list    

class PostDetails(ListView):          #context :post ,object
    model=Post                        # tempalte:post_details 

class AddPost(CreateView):
    model=Post
    fields='__all__'                  #instaed of forms file  
    success_url='/posts/'             #instead of redirect

class EditPost(UpdateView):
    model=Post
    fields='__all__'                  #instaed of forms file  
    success_url='/posts/'             #instead of redirect
    template_name='posts/edit.html'