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
from myapp.models.message import *
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

###################################################################


###################################################################    ###################################################################
def file_upload(request):
    if request.method == 'POST':
        print("here!!!",request.FILES)
        my_file=request.FILES.get('file')
        msg=MessageFile.objects.create(msgFile=my_file)
        data=dict()
        data["id"]=msg.id
        return JsonResponse(data)
        # return HttpResponse('')
    return JsonResponse({'post':'fasle'})
class MessageUploadView(View):
    def get(self, request):
        # books = MessageFile.objects.all()
        # return render(request, 'myapp/msg_file/woFileList.html', {'woFiles': books})
        pass

    def post(self, request,Id=None):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        from django.core.exceptions import ValidationError
        data=dict()
        # fmt = getattr(settings, 'LOG_FORMAT', None)
        # lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
        company= get_object_or_404(WorkOrder, id=Id)
        # logging.basicConfig(format=fmt, level=lvl)
        # logging.debug( request.FILES)
        valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls','.gif','.aac']
        ext = os.path.splitext(request.FILES['woFile'].name)[1]
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension.')
        else:
            save_path = os.path.join(settings.MEDIA_ROOT,'documents', request.FILES['msgFile'].name)
            path = default_storage.save(save_path, request.FILES['woFile'])
            document = MessageFile.objects.create(msgFile='documents/'+request.FILES['msgFile'].name, woFileworkorder=company)
            #data = {'is_valid': True, 'name': document.woFile.name, 'url': document.woFile.url,'ext':ext,'size':" MB {0:.2f}".format(document.woFile.size/1048576)}
            # books = MessageFile.objects.filter(woFileworkorder=Id)
            # data['html_woFile_list'] = render_to_string('myapp/msg_file/partialWoFileList.html', {
            #       'msgFiles': books})
            # data['is_valid']=True

        return JsonResponse(data)






@api_view(['GET'])
def wofile_collection(request,id):
    if request.method == 'GET':
        print("reached task")
        posts = MessageFile.objects.filter(woFileworkorder=id)
        serializer = MessageFileSerializer(posts, many=True)

        return Response(serializer.data)
@api_view(['GET'])
def wofile_detail_collection(request,id):
    if request.method == 'GET':
        # print("!23")
        posts = MessageFile.objects.get(id=id)
        serializer = MessageFileSerializer(posts)

        return Response(serializer.data)

@api_view(['POST'])
def woFile_post(request,Id=None):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        from django.core.exceptions import ValidationError
        data=dict()
        print(request.FILES['woFile'],'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # fmt = getattr(settings, 'LOG_FORMAT', None)
        # lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)
        company= get_object_or_404(WorkOrder, id=Id)
        # logging.basicConfig(format=fmt, level=lvl)

        # valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls','.gif']
        # ext = os.path.splitext(request.FILES['woFile'].name)[1]
        # if not ext.lower() in valid_extensions:
        #     raise ValidationError(u'Unsupported file extension.')
        # else:
        save_path = os.path.join(settings.MEDIA_ROOT,'documents', request.FILES['woFile'].name)
        path = default_storage.save(save_path, request.FILES['woFile'])
        document = MessageFile.objects.create(woFile='documents/'+request.FILES['woFile'].name, woFileworkorder=company)
        #data = {'is_valid': True, 'name': document.woFile.name, 'url': document.woFile.url,'ext':ext,'size':" MB {0:.2f}".format(document.woFile.size/1048576)}
        books = MessageFile.objects.filter(woFileworkorder=Id)
        data['html_woFile_list'] = render_to_string('myapp/workorder_file/partialWoFileList.html', {
              'woFiles': books})
        data['is_valid']=True

        print("Ok!!!!!!!!!!!!!!")

        return JsonResponse(data)
