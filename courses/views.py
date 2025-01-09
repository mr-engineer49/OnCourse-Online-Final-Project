from django.shortcuts import redirect, render, get_object_or_404

from courses.forms import LessonCreationForm
from .models import Course, Lesson



def home_page(request):
    return render(request, 'courses/homepage.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/courses_details.html', {'course': course})


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