
from django.urls import path
from . import views
urlpatterns = [
    path("sms-bomber",views.index,name="SMS Bomber Page"),
]