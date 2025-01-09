from django.contrib import admin
from django.urls import path, include


# Define URL patterns for the eCourse Management app. This includes the URLs for each module (users, courses, quizzes, payments, institutions, webinars, and forums).
# The URL patterns are defined in the following order: users, courses, quizzes, payments, institutions, webinars, and forums.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('courses.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('payments/', include('payments.urls')),
    path('institutions/', include('institutions.urls')),
    path('webinars/', include('webinars.urls')),
    path('forums/', include('forums.urls')),
]