from rest_framework import serializers
from .models import *


class Current_Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Current_Products
        fields = '__all__'

class Transaction_Serialzier(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        field = '__all__'
