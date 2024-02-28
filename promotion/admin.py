from django.contrib import admin
from .models import promotion
from .forms import PromotionForm

class PromotionAdmin(admin.ModelAdmin):
    form = PromotionForm

admin.site.register(promotion, PromotionAdmin)