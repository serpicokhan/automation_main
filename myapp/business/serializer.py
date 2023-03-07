from rest_framework import serializers
from myapp.models import PurchaseRequest,Purchase

class PurchaseRequestSerializer(serializers.ModelSerializer):
    PurchaseRequestRequestedUser = serializers.StringRelatedField()

    class Meta:
        model = PurchaseRequest
        fields = '__all__'
class PurchaseSerializer(serializers.ModelSerializer):
    PurchaseRequestedUser = serializers.StringRelatedField()

    class Meta:
        model = Purchase
        fields = '__all__'
class PurchaseSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['PurchaseRequestAssetMakan', 'PurchaseRequestAsset', 'PurchaseRequestPartName', 'PurchaseRequestAssetQty']
