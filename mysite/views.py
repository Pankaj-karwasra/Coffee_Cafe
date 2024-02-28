from django.http import HttpResponse
from django.shortcuts import render,redirect
from  ContactInfo.models import ContactInfo
#from OpenHours.views import show_open_hours
from OpenHours.models import OpenHours
from OurStory.models import OurStory
from OurVision.models import OurVision
from promotion.models import promotion
from Reservation.models import Reservation
#from .forms import ReservationForm
from datetime import datetime
#    from ContactUs.models import ContactUs
from OurClient.models import OurClient
from OurServices.models import OurServices
from Menu_HotCoffee.models import Menu_HotCoffee
from Menu_ColdCoffee.models import Menu_ColdCoffee


def my_custom_view(request):
     open_hours = OpenHours.objects.all()
     context1 = {'open_hours': open_hours}
     return render(request,'footer.html',context1)

def homepage(request):
    contact_info=ContactInfo.objects.first()
    open_hours = OpenHours.objects.all()
    context={'contact_info':contact_info,'open_hours':open_hours}
    return render(request,'index.html',context)

def home(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     context={'contact_info':contact_info,'open_hours':open_hours}
    
     return render(request,'index.html',context)

def about(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     our_story  = OurStory.objects.all()
     our_vision=OurVision.objects.all()
     context={'contact_info':contact_info,'open_hours':open_hours,'our_story':our_story,'our_vision':our_vision}
  

     return render (request,'about.html',context)

def contact(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     context={'contact_info':contact_info,'open_hours':open_hours}
     return render (request,'contact.html',context)

def menu(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     items=Menu_HotCoffee.objects.all()
     item_cold=Menu_ColdCoffee.objects.all()
     context={'contact_info':contact_info,'open_hours':open_hours,'items':items,'item_cold':  item_cold}
     return render(request,'menu.html',context)

def reservation(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     promotion_info=promotion.objects.all()
     reservation_info=Reservation.objects.all()
     if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time_str = request.POST.get('time')
        time_obj = datetime.strptime(time_str, '%I:%M %p').time()
        person = request.POST.get('person') 
        reservation_save = Reservation(name=name, email=email, date=date, time=time_obj, person=person)
        reservation_save.save()
        return redirect('thanks')
     context={'contact_info':contact_info,'open_hours':open_hours,'promotion_info':promotion_info,'reservation_info': reservation_info}
     return render(request,'reservation.html',context)

def service(request):
     contact_info=ContactInfo.objects.first()
     open_hours = OpenHours.objects.all()
     our_services=OurServices.objects.all()
     context={'contact_info':contact_info,'open_hours':open_hours,'our_services':our_services}
     return render(request,'service.html',context)

def testimonial(request):
      contact_info=ContactInfo.objects.first()
      open_hours = OpenHours.objects.all()
      client_info=OurClient.objects.all()
      context={'contact_info':contact_info,'open_hours':open_hours,'client_info':client_info}
      return render(request,'testimonial.html',context)

#def your_view(request):
    #contact_info=ContactInfo.objects.first()
    #context={'contact_info':contact_info}
    #return render(request,'contact.html',context)


'''def footerdata(request):
    open_hours = OpenHours.objects.all()
    context1 = {'open_hours': open_hours}
    return render(request, 'footer.html',context1 )'''

def thanks(request):
     return render(request,'thanks.html')

# Social media links
# this link work when we can hanlde this from server side
'''def redirect_to_twitter(request):
    return redirect('https://twitter.com/your_twitter_username')

def redirect_to_facebook(request):
    return redirect('https://facebook.com/your_facebook_page')

def redirect_to_linkedin(request):
    return redirect('https://linkedin.com/in/your_linkedin_profile')

def redirect_to_instagram(request):
    return redirect('https://instagram.com/your_instagram_account')'''