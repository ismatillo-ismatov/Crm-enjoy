from django.contrib import admin
from .models import Worker,Product,CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','is_worker')

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','worker','name',)