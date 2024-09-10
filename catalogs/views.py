from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 

def catalogs(request):
    return HttpResponse("Personal electronic accessories")