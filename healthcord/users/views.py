from django.shortcuts import render
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'users/home.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def research(request):
    return render(request, 'users/research.html')