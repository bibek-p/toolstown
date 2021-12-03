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
    return render(request,"image_converter/jpg-to-png.html")

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
    return render(request,"image_converter/png-to-jpg.html")

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
    return render(request,"image_converter/png-to-jpeg.html")

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
    return render(request,"image_converter/image-to-pdf.html")


