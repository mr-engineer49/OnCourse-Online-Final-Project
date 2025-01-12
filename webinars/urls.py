from django.urls import path
from . import views


app_name = 'webinars'

urlpatterns = [
    path('index/', views.webinar_list, name='webinar_list'),
    path('webinar/<int:webinar_pk>/details/', views.webinar_detail, name='webinar_detail'),
    path('create/', views.create_webinary, name='create_webinar'),
    path('webinar/<int:webinar_pk>/attend/', views.webinar_attend, name='webinar_attend'),
]