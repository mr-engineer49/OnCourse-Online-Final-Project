from django.shortcuts import render, get_object_or_404
from .models import Question

def quiz_detail(request, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    questions = Question.objects.filter(lesson=lesson)
    return render(request, 'quizzes/quiz_detail.html', {'questions': questions})