from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
import hashlib
import base64


def text_to_uppercase(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.upper()
        return render(request, 'text_converter/text_to_uppercase.html', {
                'output': result
            })
    return render(request,"text_converter/text_to_uppercase.html")

def text_to_lowercase(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.lower()
        return render(request, 'text_converter/text_to_lowercase.html', {
                'output': result
            })
    return render(request,"text_converter/text_to_lowercase.html")


def text_to_capitalize(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.capitalize()
        return render(request, 'text_converter/text_to_capitalize.html', {
                'output': result
            })
    return render(request,"text_converter/text_to_capitalize.html")

def word_count(request):
    if request.method == 'POST':
        text=request.POST["text"]
        word_list = text.split()
        number_of_words = len(word_list)
        result= "Total Number Of Word In Your Text Is : "+str(number_of_words)
        return render(request, 'text_converter/word_count.html', {
                'output': result
            })
    return render(request,"text_converter/word_count.html")

def remove_space(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.replace(" ",'')
        return render(request, 'text_converter/remove_space.html', {
                'output': result
            })
    return render(request,"text_converter/remove_space.html")

def replace_text(request):
    if request.method == 'POST':
        text=request.POST["text"]
        tofind=request.POST["tofind"]
        replace=request.POST["replace"]
        result = text.replace(tofind,replace)
        return render(request, 'text_converter/replace_text.html', {
                'output': result
            })
    return render(request,"text_converter/replace_text.html")


def repeat_text(request):
    if request.method == 'POST':
        text=request.POST["text"]
        nooftime=request.POST["nooftime"]
        result=""
        for i in range(int(nooftime)):
            result=result+text
        return render(request, 'text_converter/repeat_text.html', {
                'output': result
            })
    return render(request,"text_converter/repeat_text.html")


def text_reverse(request):
    if request.method == 'POST':
        text=request.POST["text"]
        return render(request, 'text_converter/text_reverse.html', {
                'output': text[::-1]
            })
    return render(request,"text_converter/text_reverse.html")

