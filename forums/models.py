from django.db import models
from courses.models import Course
from users.models import CustomUser

class Forum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='forum')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Thread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='threads')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content