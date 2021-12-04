from django.urls import path
from . import views
urlpatterns = [
    path("md5-generator",views.md5_generator,name="MD5 Generator"),
    
]