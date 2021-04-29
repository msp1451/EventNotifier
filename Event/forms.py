from django import forms
from django.contrib.auth.models import User
from django.core.checks import messages
from .models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ['title', 'event_type', 'detail', 'event_logo', 'date', 'time']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'email' : forms.TextInput(attrs={'placeholder': 'Email'}),
            'password' : forms.TextInput(attrs={'placeholder': 'Password'})
            }