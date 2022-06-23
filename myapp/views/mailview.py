'''
 fmt = getattr(settings, 'LOG_FORMAT', None)
 lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

 logging.basicConfig(format=fmt, level=lvl)
 logging.debug(nemailbject.OrderId.id)
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

from myapp.models.message import *
#from django.core import serializers
import json
from django.forms.models import model_to_dict
from myapp.forms import MessageForm
from django.urls import reverse_lazy,reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import *

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
@login_required
def list_mail(request,id=None):
    #
    books = Message.objects.filter().order_by('-id')
    wos=doPaging(request,(books))

    return render(request, 'myapp/mail/mailList.html', {'mails': wos,'title':'صندوق دریافت','section':'list_mail'})
@login_required
def list_sentmail(request):
    #
    books = Message.objects.filter(fromUser__userId=request.user).order_by('-id')
    wos=doPaging(request,(books))
    return render(request, 'myapp/mail/mailList.html', {'mails': wos,'title':'صندوق ارسال','section':'list_sentmail'})
def list_sysmail(request):
    #
    books = Message.objects.filter(fromUser__fullName="myapp").order_by('-id')
    wos=doPaging(request,(books))
    return render(request, 'myapp/mail/mailList.html', {'mails': wos,'title':'پیامهای سیستم','section':'list_sysmail'})


##########################################################

def save_mail_form(request, form, template_name):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():


            form.save()
            data['form_is_valid'] = True
            # print("&&&&&&&&&&&&&",form.instance.MessageStatus)
            books = Message.objects.filter(toUser__userId=request.user).order_by('-id')
            data['html_mail_list'] = render_to_string('myapp/mail/partialMailList.html', {
                'mails': books
            })
        else:
            data['form_is_valid'] = False
            print(form.errors)

    context = {'form': form}


    data['html_mail_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################


def mail_delete(request, id):
    comp1 = get_object_or_404(Message, id=id)
    data = dict()
    if (request.method == 'POST'):
        comp1.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        companies =  Message.objects.filter(toUser__userId=request.user).order_by('-id')
        #Tasks.objects.filter(mailId=id).update(mail=id)
        data['html_mail_list'] = render_to_string('myapp/mail/partialMaillist.html', {
            'mails': companies
        })
    else:
        context = {'mail': comp1}
        data['html_mail_form'] = render_to_string('myapp/mail/partialMailDelete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

##########################################################

##########################################################
def mail_create(request):
    if (request.method == 'POST'):
        form = MessageForm(request.POST)
        form.isupdated=False
        file_ids=request.POST.get("file_id",False)
        if form.is_valid():
            frm=form.save()
            if(file_ids):
                files=MessageFile.objects.filter(id__in=file_ids.split(','))
                for i in files:
                    i.msgFileworkorder=frm
                    i.save()

        else:
            print(form.errors)

        return HttpResponseRedirect(reverse('list_mail'))
    else:

        form = MessageForm({'fromUser':SysUser.objects.get(userId=request.user.id),'messageStatus':2})
        # form.isupdated=False
        # return save_mail_form(request, form, 'myapp/mail/partialMailCreate.html')
        return render(request, 'myapp/mail/partialMailCreate.html', {'form':form})




##########################################################
def mail_update(request, id):
    company= get_object_or_404(Message, id=id)



    template=""
    if (request.method == 'POST'):
        form = MessageForm(request.POST, instance=company)
        form.isupdated=True
    else:
        form = MessageForm(instance=company)
        company.messageStatus=3
        files=MessageFile.objects.filter(msgFileworkorder=company)
        counts=files.count()
        # company.save()



        return render(request, 'myapp/mail/partialMailUpdate.html', {'form':form,'files':files,'counts':counts,'instance':company})
    # return save_mail_form(request, form,"myapp/mail/partialMailUpdate.html")
####################list unread mail for status bar ######################################
def list_unread_mail(request):
    data = dict()
    companies =  Message.objects.filter(messageStatus=2).filter(toUser__userId=request.user)
    data["html_mail_list"]=render_to_string('myapp/mail/status.html', {
        'mails': companies,
        'count':companies.count()
    })
    return JsonResponse(data)

##########################################################
