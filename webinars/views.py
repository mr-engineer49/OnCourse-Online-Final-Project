from django.shortcuts import render, get_object_or_404
from .models import Webinar

def webinar_list(request):
    webinars = Webinar.objects.all()
    return render(request, 'webinars/webinar_list.html', {'webinars': webinars})

def webinar_detail(request, pk):
    webinar = get_object_or_404(Webinar, pk=pk)
    return render(request, 'webinars/webinar_detail.html', {'webinar': webinar})