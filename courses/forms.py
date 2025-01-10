from django import forms
from .models import Course, Lesson, Enrollment


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']

    def form_valid(self, form):
        form.instance.instructor = self.request.user  # Set the instructor as the logged-in user
        return super().form_valid(form)



class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'video_url']  




class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'course']

