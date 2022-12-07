from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(response):
    return HttpResponse("<h1>register</h1>")