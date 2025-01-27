from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('courses.urls')),
    path('quizzes/', include('quizzes.urls')),
    # path('payments/', include('payments.urls')),  # Commented out due to missing module
    path('institutions/', include('institutions.urls')),
    path('webinars/', include('webinars.urls')),
    path('forums/', include('forums.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
