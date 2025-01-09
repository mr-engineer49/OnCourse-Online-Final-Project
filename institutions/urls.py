from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.institution_list, name='institution_list'),
]