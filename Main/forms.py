from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

#Registration Form

class registrationform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': "Enter your Email"}
        # labels = {'username': forms.Textarea(attrs={'class': 'form-control'})}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

