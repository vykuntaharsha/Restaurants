from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForms
# Create your views here.


def restaurant_creatview(request):
    template_name = 'restaurants/create_restaurant_form.html'
    form = RestaurantLocationCreateForms(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors
    context = {"form": form, "errors": errors}
    return render(request,template_name,context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name=template_name, context=context)


class RestaurantListView(ListView):

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(category__contains=slug)
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForms
    template_name = 'restaurants/create_restaurant_form.html'
    success_url = '/restaurants/'
