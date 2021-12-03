from django.urls import path
from . import views
urlpatterns = [
    path("jpg-to-png",views.index,name="JPG To Png Converter"),
]