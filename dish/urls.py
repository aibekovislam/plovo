from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", DishListView.as_view(), name="dishes"),
    path('create/', DishCreateAPIView.as_view(), name="create"),
    path('<int:pk>/', DishDetailAPIView.as_view(), name="detail"),
    path('<int:pk>/delete', DishDeleteAPIView.as_view(), name="delete")
]