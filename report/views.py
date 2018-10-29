from django.shortcuts import render,redirect
from django.http import *
from .models import *
import requests





# def index(request):
#     return redirect('http://192.165.6.217:8000/#/signin?closePopupWhenDone=true&site=&authSetting=DEFAULT&siteLuid=&embedded=true')  #report/index.html


def index(request):
    return render(request,'report/index.html')  #report/index.html


#登陆
# def login():
#     session_requests = requests.session()
#     url_login = "http://192.165.6.217:8000/vizportal/api/web/v1/login"
#     datas={"method":"login","params":{"username":"ljm475599@126.com","encryptedPassword":"024643366ade89fe94c42daa390e37baf4797a292c2be6638e69306bc5af339bd6c27d36854431d41ca132d18857b4fbe406ece41b7688f64d9474581968b4b6eef2b6162fb9bfe4184e2e5f23e7ebaac6113c872b3b08dad9a079bc256a6aaf26f93c007aa79c62d7b7927aaa2663700af26a846e03da84bcd5400d6942803b","keyId":"iD9JLfD8T0a8yk4t8j4m5Q|76Xk1hiLihnyzO4NBR2MpecVvEstVNcn","siteUrlName":""}}
#     session_requests.post(url_login,data=datas)
#
#
#
