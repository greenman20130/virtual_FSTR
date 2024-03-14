from django.db import models

# Create your models here.
class Users(models.Model):
    email=models.EmailField(max_length=100)
    last_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
