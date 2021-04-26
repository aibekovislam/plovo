from django.contrib import admin
from django.urls import path
from dish.views import DishListView


urlpatterns = [
    path("",DishListView.as_view(), name="dishes"),
]