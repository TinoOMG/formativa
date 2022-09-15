from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    return HttpResponse("<h1>Chao Mundirijillo<h1>")

def display2(request):
    return HttpResponse("<h1>Se sonroja<h1>")