from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    STATUS = (
			('present', 'present'),
			('absent', 'absent'),
			('leave', 'leave'),
			)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


class Attend(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    STATUS = (
			('present', 'present'),
			
			('leave', 'leave'),
			)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    

