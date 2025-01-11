from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.forms import LessonCreationForm
from institutions.models import AvailableInstitution, Institution
from quizzes.forms import QuestionForm
from quizzes.models import Question
from .models import Course, Enrollment, Lesson



def home_page(request):
    courses = Course.objects.all()[0:3]
    enrolled_courses = set()
    if request.user.is_authenticated:
        enrolled_courses = set(Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True))

    institutions = Institution.objects.all()

    
    
    context={'courses': courses, 'enrolled_courses': enrolled_courses, 'institutions': institutions}
    return render(request, 'courses/homepage.html', context)


def course_list(request):
    """
    This function retrieves all courses from the database and prepares a list of enrolled courses for the authenticated user.
    It then renders the course list page with the retrieved data.

    Parameters:
    request (HttpRequest): The request object containing user information and other request details.

    Returns:
    HttpResponse: The rendered course list page with the context containing all courses and enrolled courses.
    """
    courses = Course.objects.all()
    enrolled_courses = set()

    if request.user.is_authenticated:
        enrolled_courses = set(Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True))

    institutions = AvailableInstitution.objects.all()
    context={'courses': courses, 'enrolled_courses': enrolled_courses, 'institutions': institutions}    
    return render(request, 'courses/course_list.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrolled = False
    if request.user.is_authenticated:
        enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    context = {
        'course': course,
        'enrolled': enrolled,
    }    
    quizz_form = Question.objects.all()
    print(quizz_form)
    return render(request, 'courses/courses_details.html', context)


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



def course_enrollment(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        Enrollment.objects.create(user=request.user, course=course)
        print("Enrolled in course:", course.title)
        return redirect('courses:course_detail', course.pk)  # Redirect to course detail page after enrollment
    else:
        print("Already enrolled in course:", course.title)
        return redirect('courses:course_list')  # Redirect to course list page if already enrolled
