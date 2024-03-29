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

#from django.core import serializers
import json
from django.forms.models import model_to_dict
from myapp.forms import AssetPartForm
from rest_framework.decorators import api_view
# from myapp.api.WOSerializer import *
from rest_framework.response import Response

###################################################################
def list_assetPart(request,id=None):
    books = WorkorderPart.objects.all()
    return render(request, 'myapp/workorder_parts/assetPartList.html', {'assetParts': books})


###################################################################
def js_list_assetPart(request,woId):
    data=dict()
    # print(woId)
    # print("here!!!!!!!!!!!!!")
    #books=AssetPart.objects.filter(assetPartAssetid=woId)
    # query="select id as id,assetPartAssetid_id,sum(assetPartQnty) as assetPartQnty from assetpart where  assetPartAssetid_id={} group by assetPartAssetid_id,AssetPartPid_id".format(woId)
    # query="select * from assetpart where assetPartAssetid_id={0}".format(woId)
    books2=BOMGroupPart.objects.filter(BOMGroupPartBOMGroup__in=
    BOMGroupAsset.objects.filter(BOMGroupAssetAsset=woId).values_list('BOMGroupAssetBOMGroup',flat=True))

    books=AssetPart.objects.filter(assetPartAssetid=woId).order_by('-id')

    data['html_assetPart_list']= render_to_string('myapp/asset_parts/partialAssetPartList.html', {
        'assetParts': books,
        'bomlist':books2
    })
    data['form_is_valid']=True
    return JsonResponse(data)


###################################################################    ###################################################################
@csrf_exempt
def save_assetPart_form(request, form, template_name,woId=None):
    data = dict()
    if (request.method == 'POST'):
          if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # fmt = getattr(settings, 'LOG_FORMAT', None)
            # lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
            # logging.basicConfig(format=fmt, level=lvl)
            # logging.debug( woId)
            # query="select id as id,assetPartAssetid_id,sum(assetPartQnty) as assetPartQnty from assetpart where  assetPartAssetid_id={} group by assetPartAssetid_id,AssetPartPid_id order by id desc".format(woId)
            books=AssetPart.objects.filter(assetPartAssetid=woId).order_by('-id')

            # books=AssetPart.objects.raw(query)
            books2=BOMGroupPart.objects.filter(BOMGroupPartBOMGroup__in=
            BOMGroupAsset.objects.filter(BOMGroupAssetAsset=woId).values_list('BOMGroupAssetBOMGroup',flat=True))
            data['html_assetPart_list'] = render_to_string('myapp/asset_parts/partialAssetPartList.html', {
                'assetParts': books,
                'bomlist':books2
            })
          else:
              pass
              # fmt = getattr(settings, 'LOG_FORMAT', None)
              # lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
              # logging.basicConfig(format=fmt, level=lvl)
              # logging.debug( form.errors)
    print('2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    context = {'form': form}
    data['html_assetPart_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
###################################################################

@csrf_exempt
def assetPart_delete(request, id):
    try:
        comp1 = get_object_or_404(AssetPart, id=id)
        data = dict()
        woId=comp1.assetPartAssetid

        if (request.method == 'POST'):
            comp1.delete()
            data['form_is_valid'] = True  # This is just to play along with the existing code
            query="select id as id,assetPartAssetid_id,sum(assetPartQnty) as assetPartQnty from assetpart where  assetPartAssetid_id={} group by assetPartAssetid_id,AssetPartPid_id order by id desc".format(woId)

            books=AssetPart.objects.raw(query)

            data['html_assetPart_list'] = render_to_string('myapp/asset_parts/partialAssetPartList.html', {
                'assetParts': books
            })
        else:
            print("1")
            context = {'assetPart': comp1}
            data['html_assetPart_form'] = render_to_string('myapp/asset_parts/partialAssetPartDelete.html',
                context,
                request=request,
            )
        return JsonResponse(data)
    except:
        data = dict()
        data['form_is_valid'] = True
        if (request.method == 'POST'):
            data['form_is_valid'] = True  # This is just to play along with the existing code
            # query="select id as id,assetPartAssetid_id,sum(assetPartQnty) as assetPartQnty from assetpart where  assetPartAssetid_id={} group by assetPartAssetid_id,AssetPartPid_id".format(woId)

            books=AssetPart.objects.filter(assetPartAssetid=woId).order_by('-id')

            # books=AssetPart.objects.raw(query)
            books2=BOMGroupPart.objects.filter(BOMGroupPartBOMGroup__in=
            BOMGroupAsset.objects.filter(BOMGroupAssetAsset=woId).values_list('BOMGroupAssetBOMGroup',flat=True))
            data['html_assetPart_list'] = render_to_string('myapp/asset_parts/partialAssetPartList.html', {
                'assetParts': books,
                'bomlist':books2
            })


        return JsonResponse(data)
###################################################################
@csrf_exempt
def assetPart_create(request):
    woId=-1
    fmt = getattr(settings, 'LOG_FORMAT', None)
    lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
    logging.basicConfig(format=fmt, level=lvl)
    logging.debug( "dasdsadasdsa")
    if (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)


        data = request.POST.dict()
        data['assetPartAssetid']=body['lastAssetid']
        data['assetPartPid']=body['assetPartPid']
        data['assetPartQnty']=body['assetPartQnty']
        data['assetPartDescription']=body['assetPartDescription']

        woId=body['lastAssetid']

        form = AssetPartForm(data)

    else:
        form = AssetPartForm()
    return save_assetPart_form(request, form, 'myapp/asset_parts/partialAssetPartCreate.html',woId)
###################################################################

@csrf_exempt
def assetPart_update(request, id):
    company= get_object_or_404(AssetPart, id=id)
    woId=company.assetPartAssetid
    if (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        data = request.POST.dict()
        data['assetPartAssetid']=body['lastAssetid']
        data['assetPartPid']=body['assetPartPid']
        data['assetPartQnty']=body['assetPartQnty']
        data['assetPartDescription']=body['assetPartDescription']
        form = AssetPartForm(data, instance=company)
    else:
        form = AssetPartForm(instance=company,initial={'mypart':company.assetPartPid.partName})
    return save_assetPart_form(request, form, 'myapp/asset_parts/partialAssetPartUpdate.html',woId.id)
@api_view(['GET'])
def assetpart_collection(request,id):
    if request.method == 'GET':
        posts = AssetPart.objects.filter(assetPartAssetid=id)
        serializer = AssetPartSerializer(posts, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def assetpart_detail_collection(request,id):
    if request.method == 'GET':
        print(id,"id")
        posts = AssetPart.objects.get(id=id)
        serializer = AssetPartSerializer(posts)
        return Response(serializer.data)
