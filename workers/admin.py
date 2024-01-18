from django.contrib import admin
from .models import Worker,Product,CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username')

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','is_worker','phone')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')