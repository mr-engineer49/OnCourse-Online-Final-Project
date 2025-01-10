from django import forms
from .models import Forum, Thread





class ForumCreateForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['course', 'name']
        # Add a custom validation rule for the title field
        def clean_title(self):
            title = self.cleaned_data['name']
            if len(title) < 10:
                raise forms.ValidationError('Title must be at least 10 characters long')
            return title



class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['forum','user','title']
