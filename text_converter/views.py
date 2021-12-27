from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
import hashlib
import base64
from datetime import datetime
import os


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

def text_file_to_json(request):
    if request.method == 'POST':
        seperator=request.POST["seperator"]
        source_media="media/"
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        myfile = request.FILES['text_file']
        main_file_name=myfile.name
        ext = main_file_name.split('.')[-1]
        if ext == "txt":
            fs = FileSystemStorage()
            uploaded_file_name=main_file_name.split('.')[0]+str(timestamp)+"."+ext
            filename = fs.save(uploaded_file_name, myfile)   
            file1 = open(source_media+filename, 'r')
            Lines = file1.readlines()
            count = 0
            mydict={}
            templist=[]
            key_list=[]
            no_of_key_found=0
            for line in Lines:
                count += 1
                if seperator in line.strip():
                    tkey=line.strip().replace(seperator,'')
                    tkey=tkey.strip()
                    mydict[tkey]={}
                    key_list.append(tkey)
                    if count != 1:
                        mydict[key_list[no_of_key_found-1]]=templist
                        templist=[]
                    no_of_key_found+=1
                
                else:
                    if line.strip() != "" and line.strip() !=" ":
                        templist.append(line.strip())
            if len(key_list) > 0:
                mydict[key_list[no_of_key_found-1]]=templist
            os.remove(source_media+filename)
            finals=str(mydict)
            finals=finals.replace("'",'"')
            return render(request, 'text_converter/text-to-json.html', {
                'output': finals
            })
        else:
            return render(request, 'text_converter/text-to-json.html', {
                'error': "You have uploaded invalid text file format"
            })
    return render(request,"text_converter/text-to-json.html")

def json_to_php_array(request):
    if request.method == 'POST':
        text=request.POST["text"]
        url = "https://jsontophp.com/"
        payload={'jayson': text}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        return render(request, 'text_converter/json-to-php-array.html', {
                'output': response.text
            })
    return render(request,"text_converter/json-to-php-array.html")
