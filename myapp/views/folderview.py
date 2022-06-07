from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Sum
import jdatetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
import django.core.serializers
import logging
from django.conf import settings
from myapp.models.users import *
from django.views import View
import json
from django.forms.models import model_to_dict
from myapp.forms import SysUserForm
# from myapp.forms import SysUserImageForm
from django.urls import reverse_lazy
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from myapp.business.mail import Mail
from myapp.business.UserUtility import *
from django.contrib.auth.decorators import login_required
from myapp.business.DateJob import *
from django.core.paginator  import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def list_folder(request):
    return render(request, 'myapp/folders/folderList.html', {})