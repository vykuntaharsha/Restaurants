from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from restaurants.models import RestaurantLocation
from menus.models import Item
# Create your views here.

User = get_user_model()


class ProfileDetailView(DetailView):
    queryset = User.objects.filter(is_active=True)
    template_name = "profiles/user.html"

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        query = self.request.GET.get('q')
        item_exists = Item.objects.filter(user=user).exists()
        queryset = RestaurantLocation.objects.filter(owner=user).search(query)
        if item_exists and queryset.exists():
            context['locations'] = queryset
        return context