from django.contrib import admin
from .models import OurServices

class OurServiesAdmin(admin.ModelAdmin):
    list_display=['image','title','description']

admin.site.register(OurServices,OurServiesAdmin)

# Register your models here.
