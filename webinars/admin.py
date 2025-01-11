from django.contrib import admin

from webinars.models import Webinar, WebinarAttendance

# Register your models here.

admin.site.register(Webinar)

admin.site.register(WebinarAttendance)