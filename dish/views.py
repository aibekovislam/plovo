from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import Dish

# Create your views here.
class DishListView(APIView):
	def get(self, request, *args, **kwargs):
		dishes = Dish.objects.order_by('name')
		dishes_serializer = DishListSerializers(dishes, many=True)
		return Response(data=dishes_serializer.data)
	#queryset = Dish.objects.order_by('name')
	#serializer_class = DishListSerializers



class DishCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DishCreatetSerializers(data=data)
        if serializer.is_valid():
            dish_object = serializer.save()
            return Response(data={'message': 'Блюдо успешно создано!'})
        return Response(data=serializer.errors)


class DishUpdateAPIView(APIView):
	def put(self, request, *args, **kwargs):
		pk = kwargs['pk']
		dish = Dish.objects.get(pk=pk)
		data =request.POST
		serializer = DishUpdateSerializersz(data=data)

		if serializer.is_valid():
			dish.name = serializer.validated_data('name')
			dish.price = serializer.validated_data('price')
			dish.save()

			serializers_object = DishSerializers(dish)

			data = serializers_object.data
			return Response(data=data)

		return Response(data={'error': 'Ошибка'})


class DishDetailAPIView(APIView):
	def get(self, request, *args, **kwargs):
		dish_object = Dish.objects.get(pk=kwargs.get('pk'))
		serializer = DishSerializers(instance=dish_object)
		return Response(data=serializer.data)


class DishDeleteAPIView(APIView):
	def delete(self, request, *args, **kwargs):
		dish = Dish.objects.get(pk=kwargs.get('pk'))
		dish.delete()
		return Response(data={'message': 'Блюдо удалено'})
