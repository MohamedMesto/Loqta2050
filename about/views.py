from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 

def about_me(request):
    return HttpResponse("about Loqta2050.com Team")