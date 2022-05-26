from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)



class Student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    student_class = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

class Exams(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=100)
    standard = models.CharField(max_length=50)
    time = models.TimeField()