from django.db import models
from home.models import *
from django.contrib.auth.models import User



# Create your models here.



class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    data_added=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
        return self.cart_id



class items(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.prod)

class checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    towncity = models.CharField(max_length=100)
    postcodezip = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=225)
    name=models.CharField(max_length=225)
    expiry_month=models.CharField(max_length=2)
    expiry_year=models.CharField(max_length=2)
    cvv=models.CharField(max_length=3)
