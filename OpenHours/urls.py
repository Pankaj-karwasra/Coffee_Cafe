from django.urls import path
from . import views

urlpatterns = [
    path('open-hours/', views.show_open_hours, name='show_open_hours'),
]