from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UpdatedUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_instructor', 'is_learner', 'is_institution', 'institution_works_for', 'available_institutions']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UpdatedUser
        fields ="__all__"
