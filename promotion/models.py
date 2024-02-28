from django.db import models

# Create your models here.
class promotion(models.Model):
    discount_percentage = models.PositiveIntegerField(default=0)
    description = models.TextField()
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)


    def formatted_discount(self):
        return f"{self.discount_percentage}% OFF"
    

    ''' def __str__(self):
        return self.title'''