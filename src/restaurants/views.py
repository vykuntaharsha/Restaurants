from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
# function based view
#
# def home(request):
#     # return HttpResponse("hello")
#     content = {
#         "content": "hello request"
#     }
#     return render(request, template_name="home.html", context=content)  # response
#
#
# def about(request):
#     content = {
#         "content": "about request"
#     }
#     return render(request, template_name="about.html", context=content)
#
#
# def contact(request):
#     content = {
#         "content": "contact request"
#     }
#     return render(request, template_name="contact.html", context=content)


# class based view


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context = {
            "content": "hello from class view"
        }

        return context
