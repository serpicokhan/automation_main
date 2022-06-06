from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
def index(request):
    today=1
    return render(request,"myapp/index.html",{"today" : today})