from django.contrib import admin
from .models import Menu_ColdCoffee


class Menu_ColfCoffee_Admin(admin.ModelAdmin):
    list_display=['image','price','title','description']

admin.site.register(Menu_ColdCoffee,Menu_ColfCoffee_Admin)