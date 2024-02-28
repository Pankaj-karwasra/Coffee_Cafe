from django.db import models

class OurServices(models.Model):
    image=models.ImageField(upload_to='service/')
    title=models.CharField(max_length=255)
    description=models.TextField()
    
