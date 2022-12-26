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
    url(r'^Purchase/items/(?P<id>\d+)$', purchase_item_get, name='purchase_item_get'),
    url(r'^PurchaseRequest/(?P<id>\d+)/update/$', purchaseRequest_update, name='purchaseRequest_update'),
    url(r'^PurchaseItem/(?P<id>\d+)/update/$', purchase_item_update, name='purchase_item_update'),
    url(r'^PurchaseItem/(?P<id>\d+)/delete/$', purchase_item_delete, name='purchase_item_delete'),
    # url(r'^PurchaseRequest/(?P<name>[-\w]+)/Search/$', searchPurchaseRequest, name='searchPurchaseRequest'),
    url(r'^PurchaseRequest/(?P<id>\d+)/delete/$', purchaseRequest_delete, name='purchaseRequest_delete'),
    url(r'^PurchaseRequest/filter/$', purchaseRequest_filter, name='purchaseRequest_filter'),
    url(r'^Part/Get/$', get_parts, name='get_parts'),

    url(r'^Asset/(?P<id>\d+)/listRelatedAsset/$', getRelatedAsset, name='getRelatedAsset'),
     url(r'^Business/$',list_business,name='list_business'),
     url(r'^Business/create/$', business_create, name='business_create'),
     url(r'^Business/(?P<id>\d+)/delete/$', business_delete, name='business_delete'),
     url(r'^Business/(?P<id>\d+)/update/$', business_update, name='business_update'),
     url(r'^Business/(?P<id>\d+)/Cancel/$', businessCancel, name='businessCancel'),
     url(r'^Business/Search/$', business_search, name='business_search'),
       url(r'^BusinessFile/$',list_businessFile,name='list_businessFile'),
      url(r'^BusinessFile/create/$', businessFile_create, name='businessFile_create'),
      url(r'^BusinessFile/(?P<id>\d+)/delete/$', businessFile_delete, name='businessFile_delete'),
      url(r'^BusinessFile/(?P<id>\d+)/update/$', businessFile_update, name='businessFile_update'),
      url(r'^BusinessFile/(?P<woId>\d+)/listBusinessFile/$', js_list_businessFile, name='js_list_businessFile'),
      url(r'^BusinessFile/(?P<Id>\d+)/basic-upload/$', BusinessFileUploadView.as_view(), name='business_upload'),

      url(r'^BusinessAsset/$',list_businessAsset,name='list_businessAsset'),
      url(r'^BusinessAsset/create/$', businessAsset_create, name='businessAsset_create'),
      url(r'^BusinessAsset/(?P<id>\d+)/delete/$', businessAsset_delete, name='businessAsset_delete'),
      url(r'^BusinessAsset/(?P<id>\d+)/update/$', businessAsset_update, name='businessAsset_update'),
      url(r'^BusinessAsset/(?P<woId>\d+)/listBusinessAsset/$', js_list_businessAsset, name='js_list_businessAsset'),

      url(r'^BusinessPart/$',list_businessPart,name='list_businessPart'),
      url(r'^BusinessPart/create/$', businessPart_create, name='businessPart_create'),
      url(r'^BusinessPart/(?P<pid>\d+)/create/$', businessPart_create, name='businessPart_create'),
      url(r'^BusinessPart/(?P<id>\d+)/delete/$', businessPart_delete, name='businessPart_delete'),
      url(r'^BusinessPart/(?P<id>\d+)/update/$', businessPart_update, name='businessPart_update'),
      url(r'^BusinessPart/(?P<woId>\d+)/listBusinessPart/$', js_list_businessPart, name='js_list_businessPart'),
      url(r'^PlanningBoard/$', list_planning_board, name='list_planning_board'),
      url(r'^Part/$',list_part,name='list_part'),
      url(r'^Part/create/$', part_create, name='part_create'),
      url(r'^Part/create2/$', part_create2, name='part_create2'),#for wopart modal form dynamic part creation
      url(r'^Part/(?P<id>\d+)/delete/$', part_delete, name='part_delete'),
      url(r'^Part/(?P<id>\d+)/update/$', part_update, name='part_update'),
      url(r'^Part/(?P<searchStr>[-\w]+)/Search/$', part_searchPart, name='part_searchPart'),
      url(r'^Part/Category/$', get_partCategory, name='get_partCategory'),
      url(r'^PartCategory/$',list_partCategory,name='list_partCategory'),
      url(r'^PartCategory/create/$', partCategory_create, name='partCategory_create'),
      url(r'^PartCategory/(?P<id>\d+)/delete/$', partCategory_delete, name='partCategory_delete'),
      url(r'^PartCategory/(?P<id>\d+)/update/$', partCategory_update, name='partCategory_update'),
      url(r'^Purchase/Record/$', record_voice, name='record_voice'),
      url(r'^Purchase/upload_file/$', file_upload, name='file_upload'),


]
