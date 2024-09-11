from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
 

def notifications(request):
    return HttpResponse("Welcome to Loqta2050 notifications Page")
