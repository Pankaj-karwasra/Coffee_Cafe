from django import forms
from .models import promotion

class PromotionForm(forms.ModelForm):
    class Meta:
        model = promotion
        fields = ['discount_percentage','description','title1','title2','title3']