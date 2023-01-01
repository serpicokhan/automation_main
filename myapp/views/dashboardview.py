from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from myapp.business.UserUtility import *
from django.contrib.auth.decorators import login_required
from myapp.models import SysUser
@login_required
def index(request):
    today=1
    UserUtility.get_user_list(request)
    return render(request,"myapp/index.html",{"today" : today})

def calendar(request):
    return render(request,"myapp/dashboard/calendar.html")
def profile(request):
    return render(request,"myapp/dashboard/profile.html")
