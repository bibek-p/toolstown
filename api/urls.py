from django.urls import path 
from . import views

urlpatterns = [
    path("headcheck",views.headcheck),
    path("create",views.createpost,name="createpost Index"),
   
   
]