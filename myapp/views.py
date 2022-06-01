from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    today=1
    return render(request,"myapp/index.html",{"today" : today})