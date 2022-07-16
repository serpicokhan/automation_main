from django.urls import path
from myapp.views import *
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView

from . import views

urlpatterns = [
    path(        'login/',        LoginView.as_view(            template_name="myapp/registration/login.html",            ),        name='login'),
    path(        'logout/',        LoginView.as_view(            template_name="myapp/registration/logout.html",            ),        name='logout'),

    path('', index, name='index'),
    url(r'^User/$',list_user,name='list_user'),
    url(r'^User/create/$', user_create, name='user_create'),
    url(r'^User/(?P<id>\d+)/update/$', user_update, name='user_update'),
    url(r'^User/(?P<id>\d+)/delete/$', user_delete, name='user_delete'),
    url(r'^Folder/$', list_folder, name='list_folder'),
    url(r'^Mail/$',list_mail,name='list_mail'),
    url(r'^Mail/create/$', mail_create, name='mail_create'),
    url(r'^Mail/(?P<id>\d+)/delete/$', mail_delete, name='mail_delete'),
    url(r'^Mail/(?P<id>\d+)/update/$', mail_update, name='mail_update'),
    url(r'^Mail/Sent/$', list_sentmail, name='list_sentmail'),
    url(r'^Mail/Status/$', list_unread_mail, name='list_unread_mail'),
    url(r'^Mail/System/$', list_sysmail, name='list_sysmail'),
    url(r'^MailFile/$', file_upload, name='file_upload'),
    url(r'^PurchaseRequest/$',list_purchaseRequest,name='list_purchaseRequest'),
    url(r'^PurchaseRequest/create/$', purchaseRequest_create, name='purchaseRequest_create'),
    # url(r'^PurchaseRequest/(?P<id>\d+)/update/$', purchaseRequest_update, name='purchaseRequest_update'),
    url(r'^PurchaseItem/create/$', purchase_item_create, name='purchase_item_create'),
    url(r'^PurchaseRequest/(?P<id>\d+)/update/$', purchaseRequest_update, name='purchaseRequest_update'),
    # url(r'^PurchaseRequest/(?P<name>[-\w]+)/Search/$', searchPurchaseRequest, name='searchPurchaseRequest'),
    url(r'^PurchaseRequest/(?P<id>\d+)/delete/$', purchaseRequest_delete, name='purchaseRequest_delete'),
    url(r'^PurchaseRequest/filter/$', purchaseRequest_filter, name='purchaseRequest_filter'),
    url(r'^Part/Get/$', get_parts, name='get_parts'),

    url(r'^Asset/(?P<id>\d+)/listRelatedAsset/$', getRelatedAsset, name='getRelatedAsset'),
]
