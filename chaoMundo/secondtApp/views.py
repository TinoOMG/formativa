from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("<h1>No hay nada<h1>")

def display2(request):
    return HttpResponse("<h1>aca tampoco<h1>")