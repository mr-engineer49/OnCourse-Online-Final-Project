from django.urls import path
from . import views


app_name = 'forums'

urlpatterns = [
    path('index/forum/', views.forum_list, name='forum_list'),
]