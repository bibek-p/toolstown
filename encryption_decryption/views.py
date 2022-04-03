from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
import hashlib
import base64
from bomber.models import ToolsDetails


def md5_generator(request):

    if request.path == "/encryption-decryption/md5-generator":
        page_details=ToolsDetails.objects.filter(toolsname="MD5 Hash Generator")
    page_details={"page_details":page_details}
    
    if request.method == 'POST':
        text=request.POST["text"]
        result = hashlib.md5(text.encode("utf-8")).hexdigest()
        page_details['output']=result
        page_details['input_text']=text
    #     return render(request, 'encryption_decryption/md5-generator.html', {
    #             'output': result,'input_text': text
    #         })

    return render(request,"encryption_decryption/md5-generator.html",page_details)

def base64_encode_decode(request):
    if request.path == "/encryption-decryption/base64-encode":
        page_details=ToolsDetails.objects.filter(toolsname="Base64 Encode")
    else:
        page_details=ToolsDetails.objects.filter(toolsname="Base64 Decode")
    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        optype=request.POST["type"]
        if optype=="encode":
            optype="Encoded"
            sample_string_bytes = text.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            result = base64_bytes.decode("ascii")

        else:
            optype="Decoded"
            base64_bytes = text.encode("ascii")
            sample_string_bytes = base64.b64decode(base64_bytes)
            result = sample_string_bytes.decode("ascii")

        page_details['output']=result
        page_details['input_text']=text
        page_details['op_type']=optype
        # return render(request, 'encryption_decryption/base64-encode-decode.html', {
        #         'output': result,'input_text': text,'op_type':optype
        #     })
    return render(request,"encryption_decryption/base64-encode-decode.html",page_details)

def ssh_generators(request):
    if request.path == "/encryption-decryption/sha512-hash-generator":
        page_details=ToolsDetails.objects.filter(toolsname="SHA512 Generator")
    if request.path == "/encryption-decryption/sha256-hash-generator":
        page_details=ToolsDetails.objects.filter(toolsname="SHA256 Generator")
    if request.path == "/encryption-decryption/sha348-hash-generator":
        page_details=ToolsDetails.objects.filter(toolsname="SHA348 Generator")
    if request.path == "/encryption-decryption/sha224-hash-generator":
        page_details=ToolsDetails.objects.filter(toolsname="SHA224 Generator")
    if request.path == "/encryption-decryption/sha1-hash-generator":
        page_details=ToolsDetails.objects.filter(toolsname="SHA1 Generator")
     

    page_details={"page_details":page_details}
    if request.method == 'POST':
        text=request.POST["text"]
        optype=request.POST["type"]
        if optype=="SHA256":
            optype="SHA256"
            result = hashlib.sha256(text.encode())
        elif optype=="SHA384":
            optype="SHA384"
            result = hashlib.sha384(text.encode())
        elif optype=="SHA224":
            optype="SHA224"
            result = hashlib.sha224(text.encode())
        elif optype=="SHA512":
            optype="SHA512"
            result = hashlib.sha512(text.encode())
        else:
            optype="SHA1"
            result = hashlib.sha1(text.encode())

        page_details['output']=result
        page_details['input_text']=text
        page_details['op_type']=optype
         

        # return render(request, 'encryption_decryption/sha-hash-generator.html', {
        #         'output': result.hexdigest(),'input_text': text,'op_type':optype
        #     })
    return render(request,"encryption_decryption/sha-hash-generator.html",page_details)


def audio_tobase64(request):
    return render(request,"encryption_decryption/audio-to-base64.html")
