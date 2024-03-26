from django.shortcuts import render
from .forms import registrationform
from django.views import View
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request,'shop.html')

def shop_detail(request):
    return render(request,'shop-detail.html')

def cart(request):
    return render(request,'cart.html')

def chackout(request):
    return render(request,'chackout.html')

def testimonial(request):
    return render(request,'testimonial.html')

def error(request):
    return render(request,'404.html')

def contract(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

class registrationView(View):
 def get(self,request):
   form=registrationform()
   return render(request,'registration.html',{'form':form})

def profile(request):
    return render(request,'profile.html')

def address(request):
    return render(request,'address.html')