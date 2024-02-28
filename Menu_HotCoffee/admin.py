from django.contrib import admin
from .models import Menu_HotCoffee

class Menu_HotCoffee_Admin(admin.ModelAdmin):
    list_display=['image','price','title','description']

admin.site.register(Menu_HotCoffee,Menu_HotCoffee_Admin)
