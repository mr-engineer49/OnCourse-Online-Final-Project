from django import forms
from .models import Course, Lesson, Enrollment


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'price']




class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'video_url']




class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'course']

