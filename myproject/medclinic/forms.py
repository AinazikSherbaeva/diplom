from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Client, Appointment


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }