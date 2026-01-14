from django.urls import path
from . import views

urlpatterns = [
    path('', views.rental_list, name='rental_list'),
]
