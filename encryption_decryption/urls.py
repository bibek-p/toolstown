from django.urls import path
from . import views
urlpatterns = [
    path("md5-generator",views.md5_generator,name="MD5 Generator"),
    path("base64-encode",views.base64_encode_decode,name="Base 64 Encode Encoded"),
    path("base64-decoded",views.base64_encode_decode,name="Base 64 Encode Decode"),
    path("sha512-hash-generator",views.ssh_generators,name="SHA-512 Hash Generator"),
    path("sha256-hash-generator",views.ssh_generators,name="SHA-256 Hash Generator"),
    path("sha384-hash-generator",views.ssh_generators,name="SHA-384 Hash Generator"),
    path("sha224-hash-generator",views.ssh_generators,name="SHA-224 Hash Generator"),
    path("sha1-hash-generator",views.ssh_generators,name="SHA-1 Hash Generator"),
    
]