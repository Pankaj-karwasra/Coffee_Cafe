from django.db import models

class Menu_ColdCoffee(models.Model):
    image=models.ImageField(upload_to='menu/')
    price = models.DecimalField(max_digits=5, decimal_places=1)
    title=models.CharField(max_length=255)
    description=models.TextField()

