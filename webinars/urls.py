from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.webinar_list, name='webinar_list'),
]