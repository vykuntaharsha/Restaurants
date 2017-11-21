from django.conf.urls import url
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
)

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create-menu-form/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
]
