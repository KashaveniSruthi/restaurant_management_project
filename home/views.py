from django.shortcuts import render

# Create your views here.
from .models import RestaurantInfo
from django.shortcuts import render
def homepage(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'home.html',{'restaurant_name':restaurant.name if restaurant else 'Our restaurant'})
def about(request):
    restaurant=RestaurantInfo.objects.first()
    return  render(request,'about.html',{
        'restaurant_name':restaurant.name if restaurant else 'Our restaurant',
        'description':restaurant.description if restaurant else '',
        'image': restaurant.image.url if restaurant and restaurant.image else ''
    })
def index(request):
    context={
        "phone"=getattar(settings,"RESTAURANT_PHONE","N/A")
    }
    return render(request,'home/index.html',context)