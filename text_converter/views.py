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
from bomber.models import ToolsDetails


def text_to_uppercase(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text To Upper Case")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.upper()
        page_details["output"]=result
        return render(request, 'text_converter/text_to_uppercase.html', page_details)
    return render(request,"text_converter/text_to_uppercase.html",page_details)

def text_to_lowercase(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text Uppercase to Lowercase")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.lower()
        page_details["output"]=result
        return render(request, 'text_converter/text_to_lowercase.html', page_details)
    return render(request,"text_converter/text_to_lowercase.html",page_details)


def text_to_capitalize(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text to Capitalization")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.capitalize()
        page_details["output"]=result
        return render(request, 'text_converter/text_to_capitalize.html', page_details)
    return render(request,"text_converter/text_to_capitalize.html",page_details)

def word_count(request):
    page_details=ToolsDetails.objects.filter(toolsname="Word Count")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        word_list = text.split()
        number_of_words = len(word_list)
        result= "Total Number Of Word In Your Text Is : "+str(number_of_words)
        page_details["output"]= result
    return render(request,"text_converter/word_count.html",page_details)

def remove_space(request):
    page_details=ToolsDetails.objects.filter(toolsname="Remove Spaces from Text")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        result = text.replace(" ",'')
        page_details["output"]= result
    return render(request,"text_converter/remove_space.html",page_details)

def replace_text(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text Replace")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        tofind=request.POST["tofind"]
        replace=request.POST["replace"]
        result = text.replace(tofind,replace)
        page_details["output"]= result
    return render(request,"text_converter/replace_text.html",page_details)


def repeat_text(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text Repeater")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        nooftime=request.POST["nooftime"]
        result=""
        for i in range(int(nooftime)):
            result=result+text
        
        page_details["output"]= result
    return render(request,"text_converter/repeat_text.html",page_details)


def text_reverse(request):
    page_details=ToolsDetails.objects.filter(toolsname="Reverse Text")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        page_details["output"]=text[::-1]
    return render(request,"text_converter/text_reverse.html",page_details)

def text_file_to_json(request):
    page_details=ToolsDetails.objects.filter(toolsname="Text File To JSON Object")
    page_details={"page_details":page_details}
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
            page_details["output"]=finals
        else:
            page_details["error"]="You have uploaded invalid text file format"
            
    return render(request,"text_converter/text-to-json.html",page_details)

def json_to_php_array(request):
    page_details=ToolsDetails.objects.filter(toolsname="JSON Object to PHP Array")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        url = "https://jsontophp.com/"
        payload={'jayson': text}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        page_details["output"]=response.text

    return render(request,"text_converter/json-to-php-array.html",page_details)
