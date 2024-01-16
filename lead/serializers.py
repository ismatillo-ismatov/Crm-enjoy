from rest_framework import serializers
from .models import Lead
from team.serializers import UserSerializer


class LeadSerializer(serializers.ModelSerializer):
    # assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Lead
        read_only_fields = ('created_by','created_date',)
        fields = ('id','team','company','phone','email','information','esdimated_value','status','priority','assigned_to',)
