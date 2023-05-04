from atexit import register
from multiprocessing import context
from re import sub
from telnetlib import AUTHENTICATION
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import regs
from django. contrib import messages
from .models import car_Booking, contact_u, car_Booking, service_Booking
import razorpay
# Create your views here.

def indexs(request):        
    if request.method == "POST":
        names=request.POST.get('naming')
        email=request.POST.get('email')
        subject=request.POST.get('Subject')
        message=request.POST.get('Message')

        contacts = contact_u(name=names, Email=email, Subject=subject, Message=message)
        contacts.save()
        messages.success(request,'Your response has been submitted ')
    return render(request,'indexs.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'login success')
            return redirect('home')
        else:
            messages.success(request, 'user_name or password is incorrect')
            return redirect('login_user')

    context = {}
    return render(request,'login_user.html',context)
         
def logoutuser(request):
    logout(request)
    return redirect('home')
          
def regss(request):
    form=regs() 
    if request.method =="POST":
            form=regs(request.POST)     
            if form.is_valid():
                form.save()   
                messages.success(request, 'Register success')
                return redirect('login_user')
    context={'form':form}
    return render(request,'regss.html',context)

def contact(request):        
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('num')
        service_type=request.POST.get('services')
        date=request.POST.get('date')
        special_request=request.POST.get('spl_req')


        services = service_Booking(name=name, email=email,phone_number=phone_number, service_type=service_type, date=date,special_request=special_request)
        services.save()
        messages.success(request, 'YOUR SERVICE IS BOOKED')

    return render(request,'service.html')

def car(request):
    return render(request,'car.html')

def detail(request):
    return render(request,'detail.html')

def bookings(request):
    if request.method == "POST":
        pickup_location = request.POST.get('picup_loc')
        drop_location = request.POST.get('dop_loc')
        pickup_date = request.POST.get('picup_date')
        pickup_time = request.POST.get('picup_time')
        drop_date = request.POST.get('dop_date')
        drop_time = request.POST.get('dop_time')
        car_name = request.POST.get('car_name')
        model = request.POST.get('model')
        transmission = request.POST.get('trans')
        total_driven = request.POST.get('total_driven')
        price = request.POST.get('price')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('your_email')
        mobile_number = request.POST.get('mob_num')
        aadhar_number = request.POST.get('aadhar_num')
        dl_number = request.POST.get('dl_num')
        aadhar_image = request.FILES['aadhar_pic']
        dl_image = request.FILES['dl_pic']
        card_name = request.POST.get('card_name')
        cvv  = request.POST.get('cvv')
        card_num = request.POST.get('card_num')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
             

        books = car_Booking(pickup_location=pickup_location, drop_location=drop_location, pickup_date=pickup_date, pickup_time=pickup_time, drop_date=drop_date, drop_time=drop_time, car_name=car_name, model=model, transmission=transmission, total_driven=total_driven, price=price, first_name=first_name, last_name=last_name, email=email, mobile_number=mobile_number, aadhar_number=aadhar_number, dl_number=dl_number, aadhar_image=aadhar_image, dl_image=dl_image, card_name=card_name, cvv=cvv, card_num=card_num, exp_month=exp_month, exp_year=exp_year)
        books.save()
        messages.success(request, 'YOUR ORDER HAS BEEN PLACED')
    return render(request,'bookings.html')

def payment(request):
    return render(request, 'payment.html')

def detail(request):
    return render(request, 'detail.html')

def detailtwo(request):
    return render(request, 'detailtwo.html')

def detailthree(request):
    return render(request, 'detailthree.html')

def detailfour(request):
    return render(request, 'detailfour.html')

def detailfive(request):
    return render(request, 'detailfive.html')

def detailsix(request):
    return render(request, 'detailsix.html')

def detailseven(request):
    return render(request, 'detailseven.html')

def detaileight(request):
    return render(request, 'detaileight.html')

def detailnine(request):
    return render(request, 'detailnine.html')







 

     
 
 
        
        
    
    