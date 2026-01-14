from django.shortcuts import render
from .models import CarReview

# Create your views here.

def review_list(request):
    reviews = CarReview.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})
