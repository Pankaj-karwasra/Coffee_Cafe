
'''from django.shortcuts import render, redirect

from .forms import ReservationForm

def book_table(request):
    if request.method=="POST":z
        form=ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation.html')
        else:
            print(form.errors)
    else:
        form=ReservationForm()
    return render(request,'reservation.html',{'form':form})'''