from django.urls import path
from . import views
urlpatterns = [
    path("news/<weblink>",views.details,name="Blog Details Page"),
    path("",views.index,name="Blog Index"),
    path("create",views.createpost,name="createpost Index"),
    path("headcheck",views.is_headingexits,name="headcheck Index"),

   
]