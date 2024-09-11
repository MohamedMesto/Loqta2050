from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
 

def votes(request):
    return HttpResponse("Welcome to Loqta2050 Vote Page")