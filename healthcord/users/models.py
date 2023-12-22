from django.db import models
from django.contrib.auth.models import User


# creating the patient database
class Patient(models.Model):
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.first_name

class Doctor(models.Model):
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    speciality = models.TextField()

    def __str__(self):
        return self.user.first_name

class Encounter(models.Model):
    encounter_id = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length = 10)
    age = models.CharField(max_length = 10)
    time_in_hospital  = models.CharField(max_length = 5)
    n_lab_procedures = models.IntegerField()
    n_medications = models.IntegerField()
    n_outpatient = models.IntegerField()
    n_emergency = models.IntegerField()
    n_inpatient = models.IntegerField()
    n_diagnoses = models.IntegerField()
    doctor = models.EmailField()

    def __str__(self):
        return User.objects.filter(email = self.email)[0]

