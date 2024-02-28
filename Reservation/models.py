from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField()
    time=models.TimeField()
    person=models.IntegerField()

    
