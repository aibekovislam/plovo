from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DishListSerializers
from .models import Dish

# Create your views here.
class DishListView(APIView):
	def get(self, request, *args, **kwargs):
		dishes = Dish.objects.order_by('name')
		dishes_serializer = DishListSerializers(dishes, many=True)
		return Response(data=dishes_serializer.data)