from django.contrib import admin
from .models import OurStory
# Register your models here.
class OurStoryAdmin(admin.ModelAdmin):
    list_display=['title','description']

admin.site.register(OurStory,OurStoryAdmin)