from .models import Dish
from rest_framework import serializers

class DishListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')