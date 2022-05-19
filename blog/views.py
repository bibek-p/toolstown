from django.shortcuts import render
from django.shortcuts import render
from PIL import Image
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
from django.core.files.storage import FileSystemStorage
# Create your views here.
import os 
from datetime import datetime
import img2pdf
import random
from PyPDF2 import PdfFileMerger, PdfFileReader
from bomber.models import ToolsDetails
from .models import Blogs
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, '404.html', {
                'error': "You have uploaded invalid image format"
            })
def details(request,weblink):
    page_details=Blogs.objects.filter(link=weblink)
    if len(page_details)==1:
        page_details={"page_details":page_details}
        return render(request, 'blog/blog_details.html',page_details)
    else:
        return render(request, '404.html', {
                    'error': "You have uploaded invalid image format"
                })


@csrf_exempt
def is_headingexits(request):
    if request.method == 'POST':
        req=request.body
        req=json.loads(req)
        heading_request=req["heading_request"]

    page_details=Blogs.objects.filter(original_heading=heading_request)
    if len(page_details)==0:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

@csrf_exempt
def createpost(request):
        if request.method == 'POST':
            req=request.body
            req=json.loads(req)
            print("===>",req)
            post=Blogs()
            post.original_heading= req['original_heading']
            post.blog_heading= req['blog_heading']
            
            post.blog_image= req['blog_image']
            post.publish_date= str(datetime.today().strftime("%b %d %Y"))
            post.content_source= req['content_source']
            blog_heading=req['blog_heading']
            
            blog_heading=blog_heading.replace(",","")
            blog_heading=blog_heading.replace('"',"-")
            blog_heading=blog_heading.replace("'","")
            blog_heading=blog_heading.replace(".","")
            blog_heading=blog_heading.replace("?","")
            blog_heading=blog_heading.replace(" ","-")

            if blog_heading[0]=="-":
                blog_heading = blog_heading[1:]
            if blog_heading[-1]=="-":
                blog_heading = blog_heading[:-1]

            post.link= blog_heading.lower()
            text=req['blog_content']
            text=text.split(".")
            round_para_n=round(len(text)/8)
            mainpara=""
            for i in range(1,round_para_n+1):
                first_list=text[(i-1)*8:i*8]
                para="".join(first_list)
                if i != 1:
                    mainpara=mainpara+".<br><br>"+para
                else:
                    mainpara=para
            restpara=text[round_para_n*8::]
            restpara="".join(restpara)
            mainpara=mainpara+".<br><br>"+restpara+" ."
            post.blog_content= mainpara
            post.save()
            return HttpResponse("====> Added New post")
                
        else:
            return HttpResponse("====>Invalid Request")
