from datetime import date
import email
from tkinter import Y
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=144)
    title = models.CharField(max_length=500)
    salary = models.CharField(max_length=99999)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=99999)
    address = models.CharField(max_length=500)
    presentaddress = models.CharField(max_length=500)
    desc = models.TextField()
    agree= models.CharField(max_length=144)
    date = models.DateField()
    def __str__(self):
        return self.name 

class Help(models.Model):
    name = models.CharField(max_length=144)
    email = models.CharField(max_length=500)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name 