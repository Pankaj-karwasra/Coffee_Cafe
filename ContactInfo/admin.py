from django.contrib import admin

# Register your models here.
from .models import ContactInfo

class contactadmin(admin.ModelAdmin):
    list_display=['address','phone','email']

admin.site.register(ContactInfo,contactadmin)