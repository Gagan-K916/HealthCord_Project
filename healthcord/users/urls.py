from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('register/', views.register , name = 'register-page')
]
