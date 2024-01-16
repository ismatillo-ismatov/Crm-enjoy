from rest_framework import serializers
from .models import Workers,Product

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('first_name','last_name','email','phone','image')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  ('user','name','cloth','color','price','size','image')