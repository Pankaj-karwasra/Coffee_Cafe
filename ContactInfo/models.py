from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return f"Contact Information"