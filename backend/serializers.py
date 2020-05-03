from rest_framework import serializers
from .models import Grocery, Pantry, Trends

class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ('groceryId', 'name', 'type', 'expirationDate', 'price', 'expiredStatus', 'pantryStatus')
        
class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ('pantryId', 'name', 'type', 'expirationDate', 'price', 'expiredStatus', 'pantryStatus')
        
class TrendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trends
        fields = ('name', 'type', 'price', 'expiredStatus', 'pantryStatus', 'month')
        
