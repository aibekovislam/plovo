from .models import Dish
from rest_framework import serializers

class DishListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'calories')

class DishCreatetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price', 'calories') 

class DishUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price', 'calories')   

class DishSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price', 'calories')