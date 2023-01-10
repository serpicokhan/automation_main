'''
 fmt = getattr(settings, 'LOG_FORMAT', None)
 lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

 logging.basicConfig(format=fmt, level=lvl)
 logging.debug(nepurchaseRequestbject.OrderId.id)
 '''
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
from django.contrib.auth.context_processors import PermWrapper
from myapp.models.purchaserequest import *
from myapp.models.users import *
#from django.core import serializers
import json
from django.forms.models import model_to_dict
from myapp.forms import PurchaseRequestForm
from myapp.forms import PurchaseForm
from django.urls import reverse_lazy,reverse
from django.db import transaction
from django.core.paginator import *
from myapp.business.UserUtility import *
from myapp.utils import *
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage





def filter_user(request):
    if(request.user.username=="admin"):
        return Purchase.objects.all().order_by('-id')
    else:
        return Purchase.objects.filter(PurchaseRequestedUser__userId=request.user).order_by('-id')
##########################################################
def list_purchaseRequest(request,id=None):
    #
    books1 = filter_user(request)
    books=doPaging(request,books1)

    return render(request, 'myapp/purchase_request/purchaseRequestList.html', {'rfq': books,'status':Status})

def save_purchaseRequest_form(request, form, template_name,id=None):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():
            form.save(commit=False)
            if(not form.instance.PurchaseRequestStatus):
                form.instance.PurchaseRequestStatus=1;

            # form.instance.PurchaseRequestRequestedUser=SysUser.objects.get(userId=request.user)
            form.save()
            # print(form.instance.PurchaseRequestDateTo,"tarikh")
            data['form_is_valid'] = True

            books1 =filter_user(request)
            books=doPaging(request,books1)
            data['html_purchaseRequest_list'] = render_to_string('myapp/purchase_request/partialPurchaseRequestList.html', {
                'rfq': books
            })
        else:
            data['form_is_valid'] = False
    title=None
    # if(form.instance.PurchaseRequestRequestedUser):
    #         title=form.instance.PurchaseRequestRequestedUser

    context = {'form': form,'title':title,'is_manager':UserUtility.is_manager(request.user)}


    data['html_purchaseRequest_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def purchaseRequest_delete(request, id):
    comp1 = get_object_or_404(PurchaseRequest, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        # companies =  PurchaseRequest.objects.all().order_by('-id')
        books1 =filter_user(request)
        books=doPaging(request,books1)
        #Tasks.objects.filter(purchaseRequestId=id).update(purchaseRequest=id)
        data['html_purchaseRequest_list'] = render_to_string('myapp/purchase_request/partialPurchaseRequestList.html', {
            'rfq': books
        })
    else:
        context = {'purchaseRequest': comp1}
        data['html_purchaseRequest_form'] = render_to_string('myapp/purchase_request/partialPurchaseRequestDelete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
def purchase_item_delete(request, id):
    comp1 = get_object_or_404(PurchaseRequest, id=id)

    data = dict()
    if (request.method == 'POST'):

        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        data['delete']=True
        data['id']=id
        # companies =  PurchaseRequest.objects.all().order_by('-id')
        # books1 =filter_user(request)

        #Tasks.objects.filter(purchaseRequestId=id).update(purchaseRequest=id)
        # data['html_purchaseRequest_list'] = render_to_string('myapp/purchase/partialPurchaseRequestList.html', {
        #     'rfq': books
        # })
    else:
        context = {'purchaseRequest': comp1}
        data['html_purchaseRequest_form'] = render_to_string('myapp/purchase/partialPurchaseRequestDelete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

##########################################################

##########################################################
def purchaseRequest_create(request):
    if (request.method == 'POST'):
        print(request.POST)
        form = PurchaseForm(request.POST)
        if(form.is_valid()):
            instance=form.save()
            item_ids=request.POST.get('lastPurchaseRequestid',False)
            if(item_ids):
                items=item_ids.split(',')
                for i in items:
                    obj=PurchaseRequest.objects.get(id=i)
                    obj.PurchaseRequestPurchase=Purchase.objects.get(id=instance.id)
                    obj.save()
            return HttpResponseRedirect(reverse('list_purchaseRequest'))

        else:
            print(form.errors)
        # return save_purchaseRequest_form(request, form, 'myapp/purchase_request/partialPurchaseRequestCreate.html')
    else:
        user_id=SysUser.objects.get(userId=request.user)
        # form = PurchaseRequestForm()

        form = PurchaseForm(initial={'PurchaseRequestedUser':user_id.id,'PurchaseStatus':1})
        # return save_purchaseRequest_form(request, form, 'myapp/purchase_request/partialPurchaseRequestCreate.html')
        return render(request, 'myapp/purchase_request/partialPurchaseRequestCreate.html', {'form': form})

def purchase_item_create(request):
    if (request.method == 'POST'):
        # print(request.user.id)
        form = PurchaseRequestForm(request.POST)
        # print(request.POST)
        if(form.is_valid()):
            data=dict()
            # pid=request.GET.get('lid',False)
            # if(pid):
            #     form.save(commit=False)
            #     form.instance.PurchaseRequestPurchase=Purchase.objects.get(id=pid)
            form.save(commit=False)
            form.instance.PurchaseRequestStatus=1
            form.instance.PurchaseRequestRequestedUser=SysUser.objects.get(userId=request.user)
            instance=form.save();

            data['id']=instance.id
            data['form_is_valid']=True
            return JsonResponse(data)
        else:
            print("error")
            print(form.errors)
            return HttpResponseRedirect(reverse('list_purchaseRequest'))

    else:

        form = PurchaseRequestForm()
        return save_purchaseRequest_form(request, form, 'myapp/purchase/partialPurchaseRequestCreate.html')
def purchase_item_update(request,id):
    company=get_object_or_404(PurchaseRequest,id=id)
    if (request.method == 'POST'):
        form = PurchaseRequestForm(request.POST,instance=company)
        # print(request.POST)
        if(form.is_valid()):
            data=dict()
            instance=form.save()
            # if(not instance.PurchaseRequestPurchase):

            data['id']=instance.id
            data['update']=True
            books=PurchaseRequest.objects.filter(PurchaseRequestPurchase=instance.PurchaseRequestPurchase)
            data['result']=render_to_string('myapp/purchase/partialPurchaseRequestList.html', {               'rfq': books            })
            data['form_is_valid']=True
            return JsonResponse(data)
        else:
            print("error")
            print(form.errors)
            return HttpResponseRedirect(reverse('list_purchaseRequest'))
    else:

        form = PurchaseRequestForm(instance=company,initial={'mypart':company.PurchaseRequestPartName.partName})
        data=dict()

        context = {'form': form}
        template_name="myapp/purchase/partialPurchaseRequestUpdate.html"
        data['html_purchaseRequest_form'] = render_to_string(template_name, context, request=request)
        return JsonResponse(data)

def purchase_item_get(request,id):
    data=dict()
    books=PurchaseRequest.objects.filter(PurchaseRequestPurchase=id)
    data['form_is_valid']=True
    data['rows']=render_to_string('myapp/purchase/partialPurchaseRequestList.html', {               'rfq': books            })
    # print("here!!!")
    return JsonResponse(data)



##########################################################
def purchaseRequest_update(request, id):
    company= get_object_or_404(Purchase, id=id)
    template=""
    if (request.method == 'POST'):
        print(request.POST)
        form = PurchaseForm(request.POST,instance=company)
        if(form.is_valid()):
            instance=form.save()
            item_ids=request.POST.get('lastPurchaseRequestid',False)

            if(item_ids):
                items=item_ids.split(',')
                for i in items:
                    obj=PurchaseRequest.objects.get(id=i)
                    obj.PurchaseRequestPurchase=Purchase.objects.get(id=instance.id)
                    obj.save()
            # print(item_ids.split(','),'!!!!!!!!!!!!!!!!!!!!!')
            # print("form is saved!!!!!!!!!!!!")


            return HttpResponseRedirect(reverse('list_purchaseRequest'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('list_purchaseRequest'))

    else:
        form = PurchaseForm(instance=company)
        file_attachment=RequestFile.objects.all()
        voices=RequestVoice.objects.all()
        return render(request, 'myapp/purchase_request/partialPurchaseRequestUpdate.html', {'form': form,'lid':id,'files':file_attachment,'voices':voices})



    # return save_purchaseRequest_form(request, form,"myapp/purchase_request/partialPurchaseRequestUpdate.html",id)
##########################################################

##########################################################


def doPaging(request,books):
    page=request.GET.get('page',1)
    paginator = Paginator(books, 10)
    wos=None
    try:
        wos=paginator.page(page)
    except PageNotAnInteger:
        wos = paginator.page(1)
    except EmptyPage:
        wos = paginator.page(paginator.num_pages)
    return wos
def purchaseRequest_filter(request):
    q=request.GET.get("q",None)
    if(q):
        books1 = filter_user(request)
        books1=books1.filter(PurchaseRequestStatus=int(q))
        books=doPaging(request,books1)
        return render(request, 'myapp/purchase_request/purchaseRequestList.html', {'rfq': books,'status':Status,'selected':int(q)})
@csrf_exempt
def record_voice(request):
    print("!!!!!!!!!!!!!!!!!")
    # print(request)
    # print(request.POST)
    print(request.FILES)
    file = request.FILES['file']
    # file_name = default_storage.save(file.name, file)
    msg=RequestVoice.objects.create(msgFile=file)

    print("!!!!!!!!!!!!!!!")
    data=dict()
    data["html_response"]=msg.msgFile.url
    data["html_name"]=msg.get_name()
    data["html_id"]=msg.id
    return JsonResponse(data)


def list_item_view(request):
    items=PurchaseRequest.objects.all().order_by('-id')
    books=doPaging(request,items)
    return render(request,"myapp/purchase_request/purchaseItemList.html",{'items':books})
@csrf_exempt
def file_upload(request):
    # def iter_rows(ws):
    #     for row in ws.iter_rows():
    #         yield [cell.value for cell in row]

    # msg=MessageFile.objects.create(msgFile=my_file)
    #     workbook = load_workbook(filename='media/'+msg.msgFile.name)
    if request.method == 'POST':
        # print("here!!!",request.FILES)
        my_file=request.FILES.get('file')
        msg=RequestFile.objects.create(msgFile=my_file)
    data=dict()
    return JsonResponse(data)
@csrf_exempt
def change_purchase_item_status(request):
    # return False
    q=request.GET.get("q", "")
    status=request.GET.get("status", 1)

    data=dict()
    q=[int(i) for i in q.split(',') ]
    # item=PurchaseRequest
    for i in q:
        item=PurchaseRequest.objects.get(id=i)
        item.PurchaseRequestStatus=int(status)
        item.save()
        items=PurchaseRequest.objects.all()
        books=doPaging(request,items)
        data['html_purchaseRequest_list'] = render_to_string('myapp/purchase_request/partialPurchaseItemList.html', {
            'items': books
        })
        data['form_is_valid']=True
    return JsonResponse(data)
