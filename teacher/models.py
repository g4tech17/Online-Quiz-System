from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=80)

