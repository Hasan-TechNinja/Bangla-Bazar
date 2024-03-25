from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('shop/',views.shop,name='shop'),
    path('shop-detail/',views.shop_detail,name='shop-detail'),
    path('cart/',views.cart,name='cart'),
    path('chackout/',views.chackout,name='chackout'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('404/',views.error,name='404'),
    path('contract/',views.contract,name='contract')
]