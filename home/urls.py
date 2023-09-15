from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('home',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('videos',views.videos,name="videos"),
    path('hospitals',views.hospitals,name="hospitals"),
    path('appointments',views.appointments,name="appointments"),
    path('newuser',views.newuser,name="newuser"),
    path('profile',views.profile,name="profile"),
    path('delhi',views.delhi,name="delhi"),
    path('rajasthan',views.rajasthan,name="rajasthan"),
    path('jodhpur',views.jodhpur,name="jodhpur"),
    path('Mandi',views.Mandi,name="Mandi"),
    path('MSP',views.MSP,name="MSP"),
    path('Buyers',views.Buyers,name="Buyers")
]