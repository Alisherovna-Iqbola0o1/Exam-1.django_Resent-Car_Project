from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('categories/', views.category_list, name='category_list'),
]
