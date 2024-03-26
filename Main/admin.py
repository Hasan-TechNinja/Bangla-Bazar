from django.contrib import admin
from django.contrib import admin
from . models import customer
# Register your models here.

@admin.register(customer)

class customerModelAdmin(admin.ModelAdmin):
    list_display=['id','name','division','user','district','thana','vllorroad','zipcode']
