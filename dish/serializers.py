from .models import Dish
from rest_framework import serializers

class DishListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')

class DishCreatetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price') 

class DishUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price')   

class DishSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')