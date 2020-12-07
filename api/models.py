from django.db import models

# Create your models here.

class Customer_Information(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    company_position = models.CharField(max_length=100)
    appointment_time = models.CharField(max_length=100)
    additional_question = models.CharField(max_length=100)