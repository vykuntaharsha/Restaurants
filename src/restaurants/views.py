from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# function based view

def home(request):
    # return HttpResponse("hello")
    content = {
        "content": "hello request"
    }
    return render(request, template_name="home.html", context=content)  # response


def about(request):
    content = {
        "content": "about request"
    }
    return render(request, template_name="about.html", context=content)


def contact(request):
    content = {
        "content": "contact request"
    }
    return render(request, template_name="contact.html", context=content)