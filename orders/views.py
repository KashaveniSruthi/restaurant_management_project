from django.shortcuts import render

# Create your views here.
from .models import RestaurantInfo
def homepage(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'home.html',{'restaurant_name': restaurant.name if restaurant else 'Our restaurant'})