from courses.models import Course
from .models import Question, Answer 
from courses.models import Lesson
from django import forms





class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'course', 'lesson']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Extract the logged-in user from the view
        super().__init__(*args, **kwargs)
        # Filter the ForeignKey queryset to show only courses created by the user
        self.fields['course'].queryset = Course.objects.filter(instructor=user)
        self.fields['lesson'].queryset = Lesson.objects.filter(course__instructor=user)
        



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct', 'question']



