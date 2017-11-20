from django import forms
from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)


class RestaurantLocationCreateForms(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category'
        ]