from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        read_only_fields = ('created_by','created_date',)
        fields = ('id','team','company','phone','email','information','esdimated_value','status','priority')
