from rest_framework import serializers
from .models import Worker,Product,CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username')
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('user','first_name','last_name','email','phone','is_worker','image')


class ProductSerializer(serializers.ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    class Meta:
        model = Product
        fields = ('worker','name','cloth','color','price','size','image')