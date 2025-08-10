from django.shortcuts import render

# Create your views here.
from .models import RestaurantInfo
def homepage(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'home.html',{'restaurant_name':restaurant_name if restaurant else 'Our restaurant'})
def about(request):
    restaurant=RestaurantInfo.objects.first()
    return  render(requesr,'about.html',{
        'restaurant_name':restaurant_name if restaurant else 'Our restaurant'
    
    })