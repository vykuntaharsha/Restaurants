from django.conf.urls import url
from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
)

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create-restaurant-form/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
]
