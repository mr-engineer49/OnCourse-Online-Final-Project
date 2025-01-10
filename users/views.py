from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

from courses.forms import CourseCreationForm
from courses.models import Course
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def user_profile(request):
    # Display the user's profile page with their information
    is_instructor = request.user.is_instructor
    is_institution = request.user.is_institution
    is_learner = request.user.is_learner
    courses = Course.objects.filter(instructor=request.user)
    enrolled_courses = request.user.enrollments.all()
    context = {
        'is_instructor': is_instructor,
        'is_institution': is_institution,
        'is_learner': is_learner,
        'courses': courses,
        'enrolled_courses': enrolled_courses,
    }
    return render(request, 'users/user_profile.html', context)

@login_required()
def create_course(request):
    # Create a new course
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.instructor = request.user  # Set the instructor as the logged-in user
            post.save()
            return redirect('courses:course_list')
    else:
        form = CourseCreationForm()

    return render(request, 'users/form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('courses:course_list')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'users/login.html', {'error': 'Invalid username or password'}, status=401)
    else:
        login_form = UserLoginForm()
        return render(request, 'users/login.html', {'login_form': login_form}, status=200)
    


def logout(request):
    # Log out the user and redirect to the home page
    auth.logout(request)
    return redirect('/')
