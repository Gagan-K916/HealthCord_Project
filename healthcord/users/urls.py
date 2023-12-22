from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('login/', views.login , name = 'login-page'),
    path('register/', views.register, name = 'register-page'),
    path('research/', views.research, name = 'research-page'),
    path('about/', views.about, name = 'about-page')
]
