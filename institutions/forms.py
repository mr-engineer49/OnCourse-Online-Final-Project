from django import forms

from institutions.models import Institution


class CreateInstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"