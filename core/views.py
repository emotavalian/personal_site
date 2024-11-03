from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return render(request, 'core/home.html')


def about_page_view(request):
    return render(request, 'core/contact_us.html')


def contact_page_view(request):
    return render(request, 'core/about_us.html')




# Create your views here.
