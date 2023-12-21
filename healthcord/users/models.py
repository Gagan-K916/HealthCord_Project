from django.db import models
from django.contrib.auth.models import User

# creating the patient database
class Patient(models.Model):
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.first_name

