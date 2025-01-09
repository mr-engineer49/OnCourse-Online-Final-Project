from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.quiz_detail, name='quiz_detail'),
    
]