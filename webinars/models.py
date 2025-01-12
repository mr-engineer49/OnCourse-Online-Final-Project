from django.db import models
from courses.models import Course
from users.models import CustomUser

class Webinar(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='webinars', blank=True, null=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class WebinarAttendance(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='attendances')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='webinar_attendances', default=None, null=True)
    def __str__(self):
        return self.webinar.title or 'Unnamed Webinar Attendance'