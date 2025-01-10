from django.urls import path
from . import views


app_name = 'institutions'


urlpatterns = [
    path('index/', views.institution_list, name='institution_list'),
    # path('institution/<int:pk>/', views.institution_detail, name='institution_detail'),
    path('add/', views.add_institution, name='add_institution'),
]