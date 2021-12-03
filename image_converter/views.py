from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json

# Create your views here.


def index(request):
    return render(request,"image_converter/jpg-to-png.html")
