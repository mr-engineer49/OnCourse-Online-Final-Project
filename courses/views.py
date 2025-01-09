from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.forms import LessonCreationForm
from quizzes.forms import QuestionForm
from quizzes.models import Question
from .models import Course, Lesson



def home_page(request):
    return render(request, 'courses/homepage.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    quizz_form = Question.objects.all()
    print(quizz_form)
    return render(request, 'courses/courses_details.html', {'course': course, 'quizz_form': quizz_form})


def add_lesson(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    if request.method == 'POST':
        add_lesson_form = LessonCreationForm(request.POST, request.FILES)
        if add_lesson_form.is_valid():
            lesson = add_lesson_form.save(commit=False)
            lesson.course = course  # Associate the lesson with the course
            lesson.save()
            return redirect('courses:course_detail', pk=course.pk)
    else:
        add_lesson_form = LessonCreationForm()
    return render(request, 'courses/add_lesson_form.html', {'add_lesson_form': add_lesson_form, 'course': course})



def lesson_detail(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})

@login_required
def quizz_creation(request):
    # TODO: Implement quizz creation form here
    if request.method == 'POST':
        quizz_form = QuestionForm(request.POST, user=request.user)
        if quizz_form.is_valid():
            quizz_form.save()
            return redirect('courses:course_list')
        else:
            print(quizz_form.errors)
    else:
        quizz_form = QuestionForm(user=request.user)
    return render(request, 'courses/quizz_creation.html', {'quizz_form': quizz_form})


