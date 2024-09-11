from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
 

def search(request):
    return HttpResponse("Welcome to Loqta2050 Search Page")