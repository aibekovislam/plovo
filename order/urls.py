from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', OrderView.as_view(), name='Order_list'),
    path('add/', OrderCreateView.as_view(), name='Order_list'),
    path('<int:pk>', OrderView.as_view(), name='order')
]