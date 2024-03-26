from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('shop/',views.shop,name='shop'),
    path('shop-detail/',views.shop_detail,name='shop-detail'),
    path('cart/',views.cart,name='cart'),
    path('chackout/',views.chackout,name='chackout'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('error/',views.error,name='error'),
    path('contract/',views.contract,name='contract'),
    path('login/',views.login,name='login'),
    path('registration/',views.registrationView.as_view(),name='registration'),
    path('profile/',views.profile,name='profile'),
    path('address/',views.address,name='address')
]