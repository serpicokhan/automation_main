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
from myapp.models.parts import *
from myapp.models import business
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
from myapp.models.business import *
from myapp.models.purchaserequest import *

def list_planning_board(request):
    sup=Business.objects.filter(id__in=PurchaseRequest.objects.filter(PurchaseRequestStatus=1).values('supplier'))
    # print(sup.suppliers.all())
    assets=Asset.objects.filter(assetIsLocatedAt__isnull=True)

    return render(request, 'myapp/planning_board/planningBoardList.html', {'sup': sup,'assets':assets})
