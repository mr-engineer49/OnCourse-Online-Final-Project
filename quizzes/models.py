from django.db import models
from courses.models import Lesson, Course

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    

# class Quiz(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     total_questions = models.IntegerField()

#     def __str__(self):
#         return self.title
    