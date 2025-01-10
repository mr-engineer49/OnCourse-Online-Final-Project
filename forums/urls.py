from django.urls import path
from . import views


app_name = 'forums'

urlpatterns = [
    path('index/forum/', views.forum_list, name='forum_list'),
    path('forum/forum/create/thread/', views.thread_create, name='thread_create'),
    path('forum/forum/create/', views.forum_create, name='forum_create'),
]