'''
 fmt = getattr(settings, 'LOG_FORMAT', None)
 lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

 logging.basicConfig(format=fmt, level=lvl)
 logging.debug(newobject.OrderId.id)
 '''

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
import os
import jdatetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
import django.core.serializers
import logging
from django.conf import settings
from myapp.models.Asset import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
#from django.core import serializers
import json
from django.forms.models import model_to_dict
# from myapp.forms import WoFileForm
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.context_processors import PermWrapper
from rest_framework.decorators import api_view
# from myapp.api.WOSerializer import *
from rest_framework.response import Response
from myapp.business.partutility import *
###################################################################


###################################################################
###################################################################
def getRelatedAsset(request,id):
    data=dict()
    assets=Asset.objects.filter(assetIsLocatedAt__id=id)
    data["pval"]=render_to_string('myapp/maintenance/partialWOAssetDynamics.html',
        {'assets':assets})
    data["form_is_valid"]=True
    return JsonResponse(data)
