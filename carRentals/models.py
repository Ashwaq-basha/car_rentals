from distutils.command.upload import upload
import email
from email.message import Message
from pyexpat import model
from django.db import models

# Create your models here.

    

class contact_u(models.Model):
    name = models.CharField(max_length=30, null=True)
    Email = models.EmailField(null=True)
    Subject = models.CharField(max_length=30,null=True)
    Message = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
class car_Booking(models.Model):
    #booking details
    pickup_location = models.CharField(max_length=30,null=True)
    drop_location = models.CharField(max_length=30,null=True)
    pickup_date = models.CharField(max_length=30,null=True)
    pickup_time = models.CharField(max_length=30,null=True)
    drop_date = models.CharField(max_length=30,null=True)
    drop_time = models.CharField(max_length=30,null=True)
    #booking
    car_name = models.CharField(max_length=30,null=True)
    model = models.CharField(max_length=30,null=True)
    transmission = models.CharField(max_length=30,null=True)
    total_driven = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    #personal details
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    #identity details
    aadhar_number = models.CharField(max_length=30,null=True)
    dl_number = models.CharField(max_length=30,null=True)
    aadhar_image = models.ImageField(default="",blank="true", upload_to="media/",null=True)
    dl_image = models.ImageField(default="",blank="true",null=True ,upload_to="media/")   
    
    #payment details 
    card_name = models.CharField(max_length=30,null=True)
    cvv = models.CharField(max_length=3,null=True)
    card_num= models.CharField(max_length=30,null=True)
    exp_month = models.CharField(max_length=5,null=True)
    exp_year = models.CharField(max_length=5,null=True)
    
    def __str__(self):
        return self.first_name

class service_Booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number= models.IntegerField()
    service_type = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    special_request = models.TextField(null=True)
    
    def __str__(self):
        return self.name