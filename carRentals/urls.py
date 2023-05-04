from django import views
from django.urls import path
from carRentals import views
from django.contrib import admin

admin.site.site_header = "admin login"
admin.site.site_title ="welcome to RentaCar admin"
admin.site.indexs_title ="RentaCar Administrator"


urlpatterns = [
    path('',views.indexs,name='home'),
    path('login_user',views.login_user,name='login_user'),
    path('contact',views.contact,name='contact'),
    path('index',views.indexs,name='index'),
    path('about',views.about,name="about"),
    path('service',views.service,name='service'),
    path('car',views.car,name='car'),
    path('detail',views.detail,name='detail'),
    path('bookings',views.bookings,name='bookings'),
    path('regss',views.regss,name='regss'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('payment',views.payment,name='payment'),
    path('detail',views.detail,name='detail'),
    path('detailtwo',views.detailtwo,name='detailtwo'),
    path('detailthree',views.detailthree,name='detailthree'),
    path('detailfour',views.detailfour,name='detailfour'),
    path('detailfive',views.detailfive,name='detailfive'),
    path('detailsix',views.detailsix,name='detailsix'),
    path('detailseven',views.detailseven,name='detailseven'),
    path('detaileight',views.detaileight,name='detaileight'),
    path('detailnine',views.detailnine,name='detailnine'),





]
