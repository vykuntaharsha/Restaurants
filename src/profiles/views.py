from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View
from restaurants.models import RestaurantLocation
from menus.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
# Create your views here.

User = get_user_model()


class ProfileFollowToggle(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        username_to_toggle = request.POST.get('username')
        profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return redirect(f"/u/{profile_.user.username}")


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
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        item_exists = Item.objects.filter(user=user).exists()
        queryset = RestaurantLocation.objects.filter(owner=user).search(query)
        if item_exists and queryset.exists():
            context['locations'] = queryset
        return context