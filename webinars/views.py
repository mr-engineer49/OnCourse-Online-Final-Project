from django.shortcuts import redirect, render, get_object_or_404

from webinars.forms import WebinarCreationForm
from .models import Webinar

def webinar_list(request):
    webinars = Webinar.objects.all()
    return render(request, 'webinars/webinar_list.html', {'webinars': webinars})

def webinar_detail(request, pk):
    webinar = get_object_or_404(Webinar, pk=pk)
    return render(request, 'webinars/webinar_detail.html', {'webinar': webinar})


def create_webinary(request):
    if request.method == 'POST':
        # create a new webinar
        webinar_form = WebinarCreationForm(request.POST, request.FILES)
        if webinar_form.is_valid():
            post = webinar_form.save(commit=False)
            post.instructor = request.user
            post.save()
            return redirect('webinars:webinar_list')
    else:
        webinar_form = WebinarCreationForm()
    return render(request, 'create_webinars.html', {'webinar_form': webinar_form})
