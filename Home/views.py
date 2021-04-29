from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about.html')


def contact(request):
    return render(request, 'html/contact.html')


def whats_new(request):
    return render(request, 'html/updates.html')
