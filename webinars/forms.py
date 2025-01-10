from django import forms
from .models import Webinar

class WebinarCreationForm(forms.ModelForm):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNamePlural'
        app_label = 'webinars'
        model = Webinar
        fields = '__all__'



