from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')

def register(request):
    return render(request, 'users/register.html')