from django.contrib import admin
from django.contrib import admin
from . models import customers
# Register your models here.

@admin.register(customers)

class customerModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','Contract_Number','email','division','user','district','thana','Union']
