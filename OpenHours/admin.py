from django.contrib import admin
from .models import OpenHours

class OpenHoursAdmin(admin.ModelAdmin):
    Hours_list =['day','time']

admin.site.register(OpenHours, OpenHoursAdmin)


