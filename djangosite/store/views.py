from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, this is the index view")

def detail(request):
    return HttpResponse("This is the detail view")

def electronics(request):
    return HttpResponse("This is the electronics view")
