from django.db import models

# Create your models here.
class OurClient(models.Model):
    client_name=models.CharField(max_length=200)
    profession=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to='testimonials/')