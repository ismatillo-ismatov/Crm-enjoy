from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Workers(models.Model):
    user = models.ForeignKey(User,related_name="workers",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/user',blank=True,null=True)

    def __str__(self):
        return self.first_name




class Product(models.Model):
    user = models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cloth = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/product')


    def __str__(self):
        return self.name





