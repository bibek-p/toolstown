from django.shortcuts import render
from PIL import Image
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
from django.core.files.storage import FileSystemStorage
# Create your views here.
import os 

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        source_media="'media/'"
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        img = Image.open(+filename)
        png_filename=img.save(source_media+os.path.splitext(filename)[0]+".png")
        uploaded_file_url = fs.url(png_filename)
        os.remove(source_media+filename)
        return render(request, 'image_converter/jpg-to-png.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request,"image_converter/jpg-to-png.html")
