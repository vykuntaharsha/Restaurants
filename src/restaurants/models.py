from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from .utils import unique_slug_generator
from .validators import validate_category
from django.conf import settings
from django.core.urlresolvers import reverse
# Create your models here.


User = settings.AUTH_USER_MODEL


class RestaurantLocationQuerySet(models.QuerySet):
    def search(self, query):  # RestaurantLocation.objects.all.search(query='')
        if query:
            query = query.strip()
            return self.filter(
            Q(name__icontains=query)|
            Q(location__icontains=query)|
            Q(location__icontains=query)|
            Q(category__icontains=query)|
            Q(item__name__icontains=query)|
            Q(item__contents__icontains=query)
            ).distinct()
        return self


class RestaurantLocationManger(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)

    def search(self, query):  # RestaurantsLocation.objects.search()
        return self.search(query)


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120,null=True,blank=True)
    category = models.CharField(max_length=120,null=True,blank=False, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)

    objects = RestaurantLocationManger()  # add Model.objects.all()

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={'slug': self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


    # def rl_post_save_receiver(self, instance, created, *args, **kwargs):
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

    # post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)