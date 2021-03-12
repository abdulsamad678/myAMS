from django import forms
from .models import Student
from .models import Attend
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password', 'status']


class SInformation(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ['name', 'email', 'password', 'status']

class CreateUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username', 'email', 'password1', 'password2']


