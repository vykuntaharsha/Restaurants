from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm
# Create your views here.


def restaurant_creatview(request):
    template_name = 'restaurants/create_restaurant_form.html'
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
            name=form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category'),
        )
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

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id= rest_id)
    #     return obj

