from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from myapp.business.UserUtility import *
from django.contrib.auth.decorators import login_required
from myapp.models import SysUser
from myapp.forms import SysUserForm
@login_required
def index(request):
    today=1
    UserUtility.get_user_list(request)
    return render(request,"myapp/index.html",{"today" : today})

def calendar(request):
    return render(request,"myapp/dashboard/calendar.html")
def profile(request):
    user=SysUser.objects.all()[0]
    company= user

    if (request.method == 'POST'):
        # print(request.FILES)
        form = SysUserForm(request.POST,request.FILES, instance=company)
    else:
        form = SysUserForm(instance=company)
    return render(request,"myapp/dashboard/profile.html",{'form':form})
