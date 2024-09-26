from rest_framework import serializers
from .models import Dresses,AddtoCart  # Make sure to import your model

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dresses  # The model to serialize
        fields = '__all__'  # Include all fields in the model

        # Alternatively, specify only certain fields
        # fields = ['id', 'category', 'name', 'desc', 'rating', 'discount', 'price', 'sold', 'delivery', 'image'
        
class AddtoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddtoCart
        fields = '__all__'