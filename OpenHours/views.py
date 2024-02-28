from django.shortcuts import render
from .models import OpenHours

def show_open_hours(request):
    open_hours = OpenHours.objects.all()
    context1 = {'open_hours': open_hours}
    return render(request, 'footer.html',context1 )
