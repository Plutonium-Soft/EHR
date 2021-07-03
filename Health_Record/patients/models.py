from pyexpat import model
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField(auto_now=True)
    gender = models.CharField(10)
    blood_group = models.CharField(10)
    insurance_no = models.CharField(50)
    address = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()