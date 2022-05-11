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

def jeg_to_png(request):
    if request.method == 'POST' and request.FILES['myfile']:
        source_media="media/"
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        myfile = request.FILES['myfile']
        main_file_name=myfile.name
        ext = main_file_name.split('.')[-1]
        if ext == "jpg" or ext == "jpeg" or ext == "JPEG" or ext == "JPG":
            fs = FileSystemStorage()
            uploaded_file_name=main_file_name.split('.')[0]+str(timestamp)+"."+ext

            filename = fs.save(uploaded_file_name, myfile)

            img = Image.open(source_media+filename)
            png_filename=img.save(source_media+os.path.splitext(filename)[0]+".png")
            uploaded_file_url = fs.url(png_filename)

            os.remove(source_media+filename)
            return render(request, 'image_converter/jpg-to-png.html', {
                'uploaded_file_url': uploaded_file_url+os.path.splitext(filename)[0]+".png"
            })
        else:
            return render(request, 'image_converter/jpg-to-png.html', {
                'error': "You have uploaded invalid image format"
            })
    page_details=ToolsDetails.objects.filter(toolsname="JPG To PNG or JPEG to PNG")
    page_details={"page_details":page_details}
    return render(request,"image_converter/jpg-to-png.html",page_details)

def png_to_jpg(request):
    if request.method == 'POST' and request.FILES['myfile']:
        source_media="media/"
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        myfile = request.FILES['myfile']
        main_file_name=myfile.name
        ext = main_file_name.split('.')[-1]
        if ext == "png" or ext == "PNG":
            fs = FileSystemStorage()
            uploaded_file_name=main_file_name.split('.')[0]+str(timestamp)+"."+ext

            filename = fs.save(uploaded_file_name, myfile)

            img = Image.open(source_media+filename)
            rgb_im = img.convert('RGB')
            png_filename=rgb_im.save(source_media+os.path.splitext(filename)[0]+".jpg")
            uploaded_file_url = fs.url(png_filename)

            os.remove(source_media+filename)
            return render(request, 'image_converter/png-to-jpg.html', {
                'uploaded_file_url': uploaded_file_url+os.path.splitext(filename)[0]+".jpg"
            })
        else:
            return render(request, 'image_converter/png-to-jpg.html', {
                'error': "You have uploaded invalid image format"
            })
    page_details=ToolsDetails.objects.filter(toolsname="PNG To JPG")
    page_details={"page_details":page_details}
    return render(request,"image_converter/png-to-jpg.html",page_details)

def png_to_jpeg(request):
    if request.method == 'POST' and request.FILES['myfile']:
        source_media="media/"
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        myfile = request.FILES['myfile']
        main_file_name=myfile.name
        ext = main_file_name.split('.')[-1]
        if ext == "png" or ext == "PNG":
            fs = FileSystemStorage()
            uploaded_file_name=main_file_name.split('.')[0]+str(timestamp)+"."+ext

            filename = fs.save(uploaded_file_name, myfile)

            img = Image.open(source_media+filename)
            rgb_im = img.convert('RGB')
            png_filename=rgb_im.save(source_media+os.path.splitext(filename)[0]+".jpeg")
            uploaded_file_url = fs.url(png_filename)

            os.remove(source_media+filename)
            return render(request, 'image_converter/png-to-jpeg.html', {
                'uploaded_file_url': uploaded_file_url+os.path.splitext(filename)[0]+".jpeg"
            })
        else:
            return render(request, 'image_converter/png-to-jpeg.html', {
                'error': "You have uploaded invalid image format"
            })
    page_details=ToolsDetails.objects.filter(toolsname="PNG To JPEG")
    page_details={"page_details":page_details}
    return render(request,"image_converter/png-to-jpeg.html",page_details)

def image_to_pdf(request):
    if request.method == 'POST' and request.FILES['myfile']:
        source_media="media/"
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        myfile = request.FILES['myfile']
        main_file_name=myfile.name
        ext = main_file_name.split('.')[-1]
        ext=ext.lower()
        if ext == "png" or ext == "jpg" or ext == "jpeg":
            fs = FileSystemStorage()

            main_file_up_name=main_file_name.split('.')[0]+str(timestamp)
            uploaded_file_name=main_file_up_name+"."+ext

            filename = fs.save(uploaded_file_name, myfile)

            img = Image.open(source_media+filename)
            

            pdf_path=source_media+main_file_name.split('.')[0]+str(timestamp)+".pdf"
            pdf_bytes = img2pdf.convert(img.filename)
            pfile = open(pdf_path, "wb")
            pfile.write(pdf_bytes)
            img.close()
            pfile.close()

            os.remove(source_media+filename)
            return render(request, 'image_converter/image-to-pdf.html', {
                'uploaded_file_url': '/media/'+main_file_up_name+".pdf"
            })
        else:
            return render(request, 'image_converter/image-to-pdf.html', {
                'error': "You have uploaded invalid image format. Allowed Format Are JPG,JPEG,PNG."
            })
    page_details=ToolsDetails.objects.filter(toolsname="Image To PDF")
    page_details={"page_details":page_details}
    return render(request,"image_converter/image-to-pdf.html",page_details)


def merge_pdf(request):
    if request.method == 'POST':
        mergedObject = PdfFileMerger()
        total_uploaded_files=[]
        print("==============>",len(request.FILES.getlist("files")))
        for count, f in enumerate(request.FILES.getlist("files")):
            curr_dt = datetime.now()
            timestamp = int(round(curr_dt.timestamp()))
            file_name='media/pdf_'+str(timestamp)+str(random.randint(0,20))+'.pdf'
            total_uploaded_files.append(file_name)
            with open(file_name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk) 
            mergedObject.append(PdfFileReader(file_name, 'r'))
            
        curr_dt = datetime.now()
        timestamp = int(round(curr_dt.timestamp()))
        output_pdf_merge="your_merge_pdf_"+str(timestamp)+str(random.randint(0,100))+".pdf"
        mergedObject.write(output_pdf_merge)
        for i in range(len(total_uploaded_files)):
            os.remove(total_uploaded_files[i])
        return HttpResponse("File(s) uploaded!")
    else:
        return render(request,"image_converter/merge-pdf.html")
    




