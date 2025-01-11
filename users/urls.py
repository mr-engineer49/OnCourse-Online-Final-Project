from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('index/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('create_course/', views.create_course, name='create_course'),
    path('update_profile/', views.user_update, name='user_update'),
]