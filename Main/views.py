from django.shortcuts import render
from .forms import registrationform,cprofile
from django.views import View
from django.contrib import messages
from .models import customers 
from django.http import HttpResponseRedirect
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
 def post(self,request):
     form=registrationform(request.POST)
     if form.is_valid():
      form.save()
      messages.success(request,'Succesfully Registration Done')
     return render(request,'registration.html',{'form':form})

class cprofileView(View):
 def get(self,request):
  form=cprofile()
  return render(request,'profile.html',{'form':form})
 
 def post(self,request):
    form=cprofile(request.POST)
    if form.is_valid():
       user=request.user
       f_name=form.cleaned_data['first_name']
       l_name=form.cleaned_data['last_name']
       em=form.cleaned_data['email']
       con=form.cleaned_data['Contract_Number']
       div=form.cleaned_data['division']
       dis=form.cleaned_data['district']
       thana=form.cleaned_data['thana']
       un=form.cleaned_data['Union']

       pro=customers(user=user,first_name=f_name,last_name=l_name,Contract_Number=con,email=em,division=div,district=dis, thana=thana,Union=un)

       pro.save()
       return HttpResponseRedirect('/address/')
    return render(request,'profile.html',{'form':form})
    

def address(request):
    add=customers.objects.filter(user=request.user)
    return render(request,'address.html',{'add':add})

def users(request):
   return render(request,'users.html')