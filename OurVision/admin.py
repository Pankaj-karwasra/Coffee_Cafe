from django.contrib import admin
from .models import OurVision

class OurVisionAdmin(admin.ModelAdmin):
    list_display=['desciption','title1','title2','title3']

admin.site.register(OurVision,OurVisionAdmin)

# Register your models here.
