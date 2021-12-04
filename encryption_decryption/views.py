from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
import hashlib


def md5_generator(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = hashlib.md5(text.encode("utf-8")).hexdigest()
        return render(request, 'encryption_decryption/md5-generator.html', {
                'output': result
            })

    return render(request,"encryption_decryption/md5-generator.html")