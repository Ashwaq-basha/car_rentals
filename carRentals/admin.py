from tokenize import group
from django.contrib import admin
from carRentals.models import contact_u, car_Booking,service_Booking
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Group)
admin.site.unregister(Group)
admin.site.register(contact_u)
admin.site.register(car_Booking)
admin.site.register(service_Booking)
