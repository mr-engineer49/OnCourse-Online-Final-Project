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
        fields = ['forum', 'user','title']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop the 'user' argument from kwargs
        super().__init__(*args, **kwargs)
        if user:
            # Filter the forum queryset to show only forums belonging to the user
            self.fields['forum'].queryset = Forum.objects.filter(user=user)
