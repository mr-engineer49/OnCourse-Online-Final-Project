from django.urls import path
from . import views


app_name = 'forums'

urlpatterns = [
    path('index/', views.forum_detail, name='forum_detail'),
]