from rest_framework import serializers
from myapp.models import PurchaseRequest

class PurchaseRequestSerializer(serializers.ModelSerializer):
    PurchaseRequestRequestedUser = serializers.StringRelatedField()

    class Meta:
        model = PurchaseRequest
        fields = '__all__'
