from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .models import Item
from .forms import ItemForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "home.html", {})

        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True).order_by("-updated")

        return render(request, "menus/home-feed.html", {'object_list': qs})

class ItemListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'form.html'
    form_class = ItemForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Menu'
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'menus/detail-update-form.html'
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        name = self.get_object().name
        context['title'] = f'Update Menu: {name}'
        return context
