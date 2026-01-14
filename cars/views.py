from django.shortcuts import render
from .models import Car, CarCategory

# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def category_list(request):
    categories = CarCategory.objects.all()
    return render(request, 'cars/category_list.html', {'categories': categories})
