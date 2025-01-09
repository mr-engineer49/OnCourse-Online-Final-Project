from django.shortcuts import get_object_or_404, render
from .models import Institution

def institution_list(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/institution_list.html', {'institutions': institutions})

def institution_detail(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    return render(request, 'institutions/institution_detail.html', {'institution': institution})