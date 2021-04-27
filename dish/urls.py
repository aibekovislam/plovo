from django.contrib import admin
from django.urls import path
from dish.views import DishListView


urlpatterns = [
    path("",DishListView.as_view(), name="dishes"),
    path('create/', DishCreatetSerializers.as_view(), name="create"),
    path('<int:pk>/', DishDetailAPIView.as_view(), name="detail"),
    path('<int:pk>/update', DishUpdateAPIView.as_view(), name="update"),
    path('<int:pk>/delete', DishDeleteAPIView.as_view(), name="delete")
]