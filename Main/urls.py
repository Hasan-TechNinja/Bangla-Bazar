from django.contrib import admin
from django.urls import path
from . import views
from.forms import loginform,passwordchangeform
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('shop/',views.shop,name='shop'),
    path('shop-detail/',views.shop_detail,name='shop-detail'),
    path('cart/',views.cart,name='cart'),
    path('chackout/',views.chackout,name='chackout'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('error/',views.error,name='error'),
    path('contract/',views.contract,name='contract'),

    path('login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=loginform),name='login'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    path('registration/',views.registrationView.as_view(),name='registration'),
    path('profile/',views.cprofileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('users/',views.users,name='users'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=passwordchangeform),name='passwordchange'),

    path('password_change/done//',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='password_change_done')



    




    

]