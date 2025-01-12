from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from webinars.forms import WebinarCreationForm
from .models import Webinar, WebinarAttendance

def webinar_list(request):
    webinars = Webinar.objects.all()
    attended_webinars = set()
    if request.user.is_authenticated:
        attended_webinars = set(WebinarAttendance.objects.filter(user=request.user).values_list('webinar_id', flat=True))
    
    return render(request, 'webinar_list.html', {'webinars': webinars, 'attended_webinars': attended_webinars})

def webinar_detail(request, webinar_pk):
    webinar_detail = get_object_or_404(Webinar, pk=webinar_pk)
    attendes = WebinarAttendance.objects.filter(webinar=webinar_detail).values().count()
    return render(request, 'webinar_details.html', {'webinar_detail': webinar_detail, 'attendes': attendes})


def create_webinary(request):
    if request.method == 'POST':
        # create a new webinar
        webinar_form = WebinarCreationForm(request.POST, request.FILES)
        if webinar_form.is_valid():
            post = webinar_form.save(commit=False)
            post.instructor = request.user
            post.save()
            return redirect('users:user_profile')
    else:
        webinar_form = WebinarCreationForm()
    return render(request, 'create_webinars.html', {'webinar_form': webinar_form})


def webinar_attend(request, webinar_pk):
    webinar = get_object_or_404(Webinar, pk=webinar_pk)
    if not WebinarAttendance.objects.filter(user=request.user, webinar=webinar).exists():
        WebinarAttendance.objects.create(user=request.user, webinar=webinar)
        print("Enrolled in webinar :", webinar.title)
        return redirect('users:user_profile')  # Redirect to course detail page after enrollment
    else:
        print("Already enrolled in course:", webinar.title)
        return redirect('users:user_profile') 
        
