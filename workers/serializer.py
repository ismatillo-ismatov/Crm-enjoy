from rest_framework import serializers
from .models import Worker,Product,CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','is_worker')
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields =('__all__')
        # fields = ('id','user','first_name','last_name','email','phone','image')


class ProductSerializer(serializers.ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    class Meta:
        model = Product
        fields = ('worker','name','cloth','color','price','size','image')