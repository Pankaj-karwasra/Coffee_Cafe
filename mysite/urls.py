"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from OpenHours.views import show_open_hours 
from django.urls import path, include
#from Reservation.views import reservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="homepage"),
    path('home', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('menu', views.menu,name='menu'),
    path('reservation',views.reservation,name='reservation'),
    path('service',views.service,name='service'),
    path('testimonial',views.testimonial,name='testimonial'),
    #path('footerdata', views.footerdata, name='footerdata'),
    path('', include('OpenHours.urls')),
    #path('', include('Reservation.urls'))
    path('thanks', views.thanks,name='thanks'),
    
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Social media links urls
# this link work when we can hanlde this from server side
'''urlpatterns = [
    # ... other URL patterns ...

    path('twitter/', views.redirect_to_twitter, name='redirect_to_twitter'),
    path('facebook/', views.redirect_to_facebook, name='redirect_to_facebook'),
    path('linkedin/', views.redirect_to_linkedin, name='redirect_to_linkedin'),
    path('instagram/', views.redirect_to_instagram, name='redirect_to_instagram'),
]'''