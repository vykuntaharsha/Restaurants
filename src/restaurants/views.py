from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation
# Create your views here.


def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name=template_name, context=context)


class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'


class BurgerRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='burgers')
    template_name = 'restaurants/restaurants_list.html'


class ChickenRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__contains='Chicken')
    template_name = 'restaurants/restaurants_list.html'
