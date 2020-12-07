from rest_framework import serializers
from .models import Customer_Information

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Information
        fields = '__all__'
        