from django.urls import path
from . import views
urlpatterns = [
    path("jpg-to-png",views.jeg_to_png,name="JPG To Png Image Converter"),
    path("jpeg-to-png",views.jeg_to_png,name="JPEG To Png Image Converter"),
    path("png-to-jpg",views.png_to_jpg,name="Png To JPG Image Converter"),
    path("png-to-jpeg",views.png_to_jpeg,name="Png To JPEG Image Converter"),
    path("image-to-pdf",views.image_to_pdf,name="Image To PDF Converter"),
]