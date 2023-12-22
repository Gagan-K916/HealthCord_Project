from django.contrib import admin
from django.contrib.auth.models import User
from .models import Patient, Doctor, Encounter

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Encounter)