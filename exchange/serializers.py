from rest_framework import serializers
from .models import Material, Seller


class MaterialSerializer(serializers.ModelSerializer):

    seller_name = serializers.CharField(source='seller.name', read_only=True)

    class Meta:
        model = Material
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
