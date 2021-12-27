from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
import hashlib
import base64


def md5_generator(request):
    if request.method == 'POST':
        text=request.POST["text"]
        result = hashlib.md5(text.encode("utf-8")).hexdigest()
        return render(request, 'encryption_decryption/md5-generator.html', {
                'output': result,'input_text': text
            })
    return render(request,"encryption_decryption/md5-generator.html")

def base64_encode_decode(request):
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

        return render(request, 'encryption_decryption/base64-encode-decode.html', {
                'output': result,'input_text': text,'op_type':optype
            })
    return render(request,"encryption_decryption/base64-encode-decode.html")

def ssh_generators(request):
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
         

        return render(request, 'encryption_decryption/sha-hash-generator.html', {
                'output': result.hexdigest(),'input_text': text,'op_type':optype
            })
    return render(request,"encryption_decryption/sha-hash-generator.html")


def audio_tobase64(request):
    return render(request,"encryption_decryption/audio-to-base64.html")
