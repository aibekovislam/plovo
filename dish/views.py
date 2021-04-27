from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import Dish

# Create your views here.
class DishListView(ListAPIView):
	#def get(self, request, *args, **kwargs):
		#dishes = Dish.objects.order_by('name')
		#dishes_serializer = DishListSerializers(dishes, many=True)
		#return Response(data=dishes_serializer.data)
	queryset = Dish.objects.order_by('name')
	serializer_class = DishListSerializers


class DishCreatetSerializers(APIView):
	def post(self, request, *args, **kwargs):
		data = request.POST
		serializer = DishCreateSerializers(data=data)
		if serializer.is_valid():
			dish_object = serializer.save()
			return Response(data={'message': 'Блюдо успешно добавлено'})
		return Response(data={'error': serializer.errors})
