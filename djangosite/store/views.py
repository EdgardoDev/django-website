from django.views import View
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.urls import path
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, request, response
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView

def index(request):
    return HttpResponse("Hello, this is the index view")

def detail(request):
    return HttpResponse("This is the detail view")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple IPhone", "Lenovo", "Samsung", "Google" )
    
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, "store/list.html", {"items": items})
    elif request.method == 'POST':
        return HttpResponseNotFound("Page not found")
