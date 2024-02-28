from django.contrib import admin
from .models import OurClient

class OurClientAdmin(admin.ModelAdmin):
    list_display=['client_name','profession','description','image']

admin.site.register(OurClient,OurClientAdmin)

# Register your models here.
