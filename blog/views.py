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
from django.template.defaultfilters import truncatewords


# Create your views here.

def index(request):
    page_details=Blogs.objects.all()[:20]
    page_details={"page_details":page_details}
    return render(request, 'blog/index.html', page_details)



def blog_cat(request,cat):
    page_details=Blogs.objects.extra(where=["LENGTH(blog_content_original) - LENGTH(REPLACE(blog_content_original, ' ', ''))+1 > %s"], params=[1000]).filter(category=cat)[:60]
    page_details_header={}
    page_details_header['page_titel']=cat.capitalize()+" News Headlines, Latest International News, World Breaking News - ToolsBand"
    page_details_header['page_description']=cat.capitalize()+" News: ToolsBand news brings the latest world news headlines, Current International breaking news world wide. In depth analysis and top news headlines world wide."
    page_details_header['keyword']=cat.capitalize()+" news, latest news, today news, breaking news, news headlines, bollywood news, India news, top news, political news, business news, technology news, sports news"
    page_details_header['author']="Bibekananda Bhuyan"
    page_details={"page_details":page_details,"page_details_header":page_details_header}
    return render(request, 'blog/index.html', page_details)


def rssfeed(request):
    now = datetime.now()

    rss_test='''<?xml version="1.0" encoding="utf-8"?>
                <rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
                    <channel>
                            <title>ToolsBand Blogs</title>
                            <link>https://toolsband.com/blog/</link>
                            <description>
                                New posts of my blog.</description>
                            <atom:link href="https://toolsband.com/blog/feed/rss" rel="self">
                            </atom:link>
                            <language>en-us</language>'''
    rss_test=rss_test+"<lastbuilddate>"+now.strftime("%d/%m/%Y %H:%M:%S")+"</lastbuilddate>"
    ress_end='</channel></rss>'
    
    feed_item=''
    page_details=Blogs.objects.all()
    for i in range(len(page_details)):
        start='<item>'
        titel='<title>'+page_details[0].blog_heading+'</title>'
        link='<link> https://toolsband.com/blog'+page_details[0].link+'</link>'
        description='<description>'+page_details[0].blog_content+'</description>'
        guid='<guid> https://toolsband.com/blog'+page_details[0].link+'</guid>'
        end='</item>'
        feed_item=feed_item+start+titel+link+description+guid+end
    
    final_feed=rss_test+feed_item+ress_end



    return HttpResponse(final_feed)



def details(request,weblink):
    page_details=Blogs.objects.filter(link=weblink)
    if len(page_details)==1:
        page_details[0].page_titel=page_details[0].blog_heading
        page_details[0].page_description= truncatewords(page_details[0].blog_content, 30) 
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
            original_heading=req['original_heading']
            original_heading=original_heading.strip()
            post.original_heading= original_heading
            post.blog_heading= req['blog_heading']
            
            post.blog_image= req['blog_image']
            post.publish_date= str(datetime.today().strftime("%b %d %Y"))
            post.content_source= req['content_source']
            blog_heading=req['blog_heading']
            twwet_quote=req["twwet_quote"]
            twwet_quote=twwet_quote.split("===>")
            
            blog_heading=blog_heading.replace(",","")
            blog_heading=blog_heading.replace('"',"-")
            blog_heading=blog_heading.replace("'","")
            blog_heading=blog_heading.replace(".","")
            blog_heading=blog_heading.replace("?","")
            blog_heading=blog_heading.replace(" ","-")
            blog_heading=blog_heading.replace("/","")
            blog_heading=blog_heading.replace("\'","")

            if blog_heading[0]=="-":
                blog_heading = blog_heading[1:]
            if blog_heading[-1]=="-":
                blog_heading = blog_heading[:-1]

            post.link= blog_heading.lower()
            text=req['blog_content']
            text=text.split(".")
            print("===>",text)
            thing="Likewise READ:"
            for i in range(len(text)):
                if len(text) > i:
                    sentense=text[i]
                    if thing in sentense:
                        text.remove(sentense)

            round_para_n=round(len(text)/8)
            mainpara=""
            for i in range(1,round_para_n+1):
                first_list=text[(i-1)*8:i*8]
                para=".".join(first_list)
                if i != 1:
                    if i <=len(twwet_quote):
                        mainpara=mainpara+".<br>"+twwet_quote[i]+"<br>"+para
                        del twwet_quote[i]
                    else:
                        mainpara=mainpara+".<br><br>"+para
                else:
                    mainpara=para
            restpara=text[round_para_n*8::]
            restpara="".join(restpara)
            mainpara=mainpara+".<br><br>"+restpara+" ."
            mainpara_origin=mainpara
            if len(twwet_quote) >0:
                for m in range(len(twwet_quote)):
                    mainpara=mainpara+twwet_quote[m]
            post.blog_content= mainpara
            post.blog_content_original=mainpara_origin
            post.keyword=req['keywords']
            post.category=req['category']
            post.save()
            return HttpResponse("====> Added New post")
                
        else:
            return HttpResponse("====>Invalid Request")
