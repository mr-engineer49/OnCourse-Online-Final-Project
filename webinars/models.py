from django.db import models
from courses.models import Course
from users.models import CustomUser

class Webinar(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(CustomUser, related_name='webinars_joined', blank=True)

    def __str__(self):
        return self.title