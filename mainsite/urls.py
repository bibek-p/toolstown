"""mainsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bomber/', include('bomber.urls')),
    path('image-converter/', include('image_converter.urls')),
    path('encryption-decryption/', include('encryption_decryption.urls')),
    path('text-converter/', include('text_converter.urls')),
    path("",views.index_home,name="Home Page"),
    path("terms-and-condition",views.terms_and_condition,name="Terms & Conditions"),
    path("privacy-policy",views.privacy_policy,name="Privacy Policy"),
    path("contact",views.contact,name="Contact Us"),
    
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "mainsite.views.page_not_found_view"