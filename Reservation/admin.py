from django.contrib import admin
from .models import Reservation
#from .forms import  ReservationForm

class ReservationAdmin(admin.ModelAdmin):
  #form = ReservationForm
  list_display=['name','email','date','time','person']

admin.site.register(Reservation,ReservationAdmin)
