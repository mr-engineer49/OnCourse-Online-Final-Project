from django import forms

from institutions.models import Institution, AvailableInstitution


class CreateInstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"


class UpdateInstitutionForm(forms.ModelForm):
    class Meta:
        model = AvailableInstitution
        fields = "__all__"

        


