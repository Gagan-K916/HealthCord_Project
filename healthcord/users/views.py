from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from .models import Encounter, Doctor, Patient



def home(request):
    return render(request, 'users/home.html')

def login(request):
    return render(request, 'users/login.html')

def about(request):
    return render(request, 'users/about.html')

def research(request):
    return render(request, 'users/research.html')
        
# <QueryDict: {'csrfmiddlewaretoken': ['hzRG1QaYJrdUOPGIB2uANOWMQGLMsiS5GLpZHNPHEVseFEPADu3Dp5P0f4Se06bl'], 'first_name': ['Gagan'], 'email': ['gagan.kulal916@gmail.com'], 'username': ['GaganK916'], 'password2': ['123'], 'password': ['123'], 'last_name': ['123']}>
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        first_name =request.POST.get('first_name','')
        last_name =request.POST.get('last_name','')
        email =request.POST.get('email','')
        username =request.POST.get('username','')
        password = request.POST.get('password','')
        user = User.objects.create_user(first_name = first_name, last_name = last_name,username=username,email=email,password=password)
        user.save()
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

