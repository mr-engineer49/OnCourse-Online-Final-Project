from django.shortcuts import get_object_or_404, redirect, render
from .models import Institution
from .forms import CreateInstitutionForm, UpdateInstitutionForm




def add_institution(request):
    # Add an institution
    if request.method == 'POST':
        institution_form = CreateInstitutionForm(request.POST)
        if institution_form.is_valid():
            institution_form.save()
            return redirect('users:user_profile')
    else:
        institution_form = CreateInstitutionForm()

    return render(request, 'form.html', {'institution_form': institution_form})



def institution_list(request):
    institutions = Institution.objects.all()
    return render(request, 'institutions/institution_list.html', {'institutions': institutions})

def institution_detail(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    return render(request, 'institutions/institution_detail.html', {'institution': institution})