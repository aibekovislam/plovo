from django.urls import path
from .views import * 

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name="user-create-list"),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView, name="user")
]