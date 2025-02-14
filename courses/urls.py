from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('courses/index/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/course/<int:course_pk>/update/', views.course_update_view, name='course_update'),
    path('courses/course/<int:course_pk>/lesson/<int:lesson_pk>/update/', views.lesson_update_view, name='lesson_update'),
    path('courses/course/<int:course_pk>/lesson/<int:lesson_pk>/delete/', views.lesson_delete_view, name='lesson_delete'),
    path('courses/course/<int:course_pk>/lesson/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('course/<int:course_pk>/add/lesson/', views.add_lesson, name='add_lesson'),
    path('courses/course/<int:course_pk>/quizz_creation/', views.quizz_creation, name='quizz_creation'),
    path('courses/enroll/<int:course_pk>/', views.course_enrollment, name='course_enrollment'),


]