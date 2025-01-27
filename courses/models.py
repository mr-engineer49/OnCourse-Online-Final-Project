from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user

class Course(models.Model):
    COURSE_CATEGORIES = (
        ('select', 'Select a category'),
        ('it', 'IT'),
        ('business', 'Business'),
        ('language', 'Language'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('science', 'Science'),
        ('politics', 'Politics'),
        ('art', 'Art'),
        ('sports', 'Sports'),
        ('history', 'History'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=10, default='select', null=True, blank=True, choices=COURSE_CATEGORIES)
    # other fields
    title = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='courses/', null=True, blank=True, default=None)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title



class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
    














    