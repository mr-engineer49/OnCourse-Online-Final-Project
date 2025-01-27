from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.forms import LessonCreationForm, CourseCreationForm
from institutions.models import AvailableInstitution, Institution
from payment_app.models import Payment
from quizzes.forms import QuestionForm
from quizzes.models import Question
from webinars.models import Webinar, WebinarAttendance
from .models import Course, Enrollment, Lesson
import random


def home_page(request):
    courses = Course.objects.all()[0:3]
    attended_webinars = set()
    if request.user.is_authenticated:
        attended_webinars = set(WebinarAttendance.objects.filter(user=request.user).values_list('webinar_id', flat=True))

        
    enrolled_courses = set()
    if request.user.is_authenticated:
        enrolled_courses = set(Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True))

    institutions = Institution.objects.all()
    webinars = Webinar.objects.all()[0:3]

    context={'courses': courses, 'enrolled_courses': enrolled_courses, 'institutions': institutions, 'webinars': webinars, 'attended_webinars': attended_webinars}
    return render(request, 'courses/homepage.html', context)


def course_list(request):
    category = request.GET.get('category')
    if category:
        courses = Course.objects.filter(category=category)
    else:
        courses = Course.objects.all()

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


def lesson_update_view(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)

    if request.method == 'POST':
        update_lesson_form = LessonCreationForm(request.POST, request.FILES, instance=lesson)
        if update_lesson_form.is_valid():
            update_lesson_form.save()
            return redirect('courses:course_detail', pk=course.pk)
    else:
        update_lesson_form = LessonCreationForm(instance=lesson)

    return render(request, 'courses/update_lesson_form.html', {'update_lesson_form': update_lesson_form, 'course': course, 'lesson': lesson})


def course_update_view(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    if request.method == 'POST':
        update_course_form = CourseCreationForm(request.POST, instance=course)
        if update_course_form.is_valid():
            update_course_form.save()
            return redirect('courses:course_detail', pk=course.pk)
    else:
        update_course_form = CourseCreationForm(instance=course)

    return render(request, 'courses/update_course_form.html', {'update_course_form': update_course_form, 'course': course})


def lesson_delete_view(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)

    lesson.delete()
    return redirect('courses:course_detail', pk=course.pk)





def lesson_detail(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})


def quizz_creation(request, course_pk):
    # TODO: Implement quizz creation form here
    if request.method == 'POST':
        quizz_form = QuestionForm(request.POST, user=request.user)
        if quizz_form.is_valid():
            quizz_form.save()
            return redirect('courses:course_list', course_id=course_pk)
        else:
            print(quizz_form.errors)
    else:
        quizz_form = QuestionForm(user=request.user)
    return render(request, 'courses/quizz_creation.html', {'quizz_form': quizz_form})



def course_enrollment(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        Enrollment.objects.create(user=request.user, course=course)
    if not Payment.objects.filter(user=request.user, billing_email=request.user.email, captured_amount=course.price, status='paid already exists', message='Payment successful already exists').exists():    
        Payment.objects.create(user=request.user, billing_email=request.user.email, transaction_id=random.randint(1000000000, 9999999999), delivery=random.randint(0, 100), tax=random.randint(0, 35), billing_first_name=request.user.first_name, billing_last_name=request.user.last_name, captured_amount=course.price, currency='USD', total=course.price, customer_ip_address=request.META.get('REMOTE_ADDR'), status='paid', message='Payment successful')
        print("Enrolled in course:", course.title)
        return redirect('courses:course_detail', course.pk)  # Redirect to course detail page after enrollment
    else:
        print("Already enrolled in course:", course.title)
        return redirect('courses:course_list')  # Redirect to course list page if already enrolled
