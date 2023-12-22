from django import forms
from django.contrib.auth.models import User



class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    

