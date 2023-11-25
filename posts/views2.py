
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from .models import Post

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


class DeletePost(DeleteView):
    model=Post
    success_url='/posts/'    