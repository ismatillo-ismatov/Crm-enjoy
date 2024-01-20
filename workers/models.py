from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    is_worker = models.BooleanField(default=False)

class Worker(models.Model):
    user = models.OneToOneField('workers.CustomUser',related_name="workers",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/user',blank=True,null=True)

    def __str__(self):
        return self.first_name




class Product(models.Model):
    worker = models.ForeignKey(Worker,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cloth = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/product',blank=True,null=True)
    add_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name





