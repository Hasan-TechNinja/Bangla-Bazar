from django.db import models
from django.contrib.auth.models import User

DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)

class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField( max_length=200)
    division=models.CharField(choices=DIVISION_CHOICES, max_length=50)
    district=models.CharField( max_length=50)
    thana=models.CharField( max_length=50)
    vllorroad=models.CharField( max_length=50)
    zipcode=models.IntegerField()

    def __str__(self):
        return str(self.id)
    
DIVISIONS_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)

class customers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField(max_length=50)
    Contract_Number=models.IntegerField()
    email=models.EmailField( max_length=254)
    division=models.CharField(choices=DIVISIONS_CHOICES, max_length=50)
    district=models.CharField( max_length=50)
    thana=models.CharField( max_length=50)
    Union=models.CharField( max_length=50)
    

    def __str__(self):
        return str(self.id)