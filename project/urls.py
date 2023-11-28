"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import post_list,post_details,create_post,edit_post,delete_post
#from posts.views2 import PostList,PostDetails,AddPost,EditPost,DeletePost
from posts.api import post_list_api,post_detailes_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',post_list),
    #path('posts/',PostList.as_view()),
    path('posts/new',create_post),
    #path('posts/new',AddPost.as_view()),
    path('posts/<int:post_id>',post_details),
    #path('posts/<int:pk>',PostDetails.as_view()),
    path('posts/<int:pk>/edit',edit_post),
    #path('posts/<int:pk>/edit',EditPost.as_view()),
    path('posts/<int:pk>/delete',delete_post),
    #path('posts/<int:pk>/delete',DeletePost.as_view()),
    path('summernote/', include('django_summernote.urls')),







   path('posts/api',post_list_api ),
   path('posts/api/<int:id>',post_detailes_api)

]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [

 ]
