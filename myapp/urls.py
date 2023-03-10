from django.urls import path
from myapp.views import *
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

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
    url(r'^Asset/$',list_asset,name='list_asset'),
    url(r'^Asset/Export/$', assetExport, name='assetExport'),
    url(r'^Asset/echo/json/$',get_json_test,name='get_json_test'),
    url(r'^Asset/WoAsset/Create$',create_woasset,name='create_woasset'),
    url(r'^Asset/Make_Row/(?P<wo>\d+)$',create_rowasset,name='create_rowasset'),
    url(r'^Asset/DASH/$',list_asset_dash,name='list_asset_dash'),
    url(r'^Asset/(?P<locId>\d+)/jslist/$',js_list_asset_dash,name='js_list_asset_dash'),
    url(r'^Asset/Location/$',list_asset_location,name='list_asset_location'),
    url(r'^Asset/Machine/$',list_asset_machine,name='list_asset_machine'),
    url(r'^Asset/Tool/$',list_asset_tool,name='list_asset_tool'),
    url(r'^Asset/Types/(?P<ids>\d+(?:,\d+)*)$',show_asset_types,name='show_asset_types'),
    url(r'^Asset/Update_Types/(?P<ids>\d+(?:,\d+)*)/(?P<cat>\d+)$',asset_type_update,name='asset_type_update'),

    url(r'^Asset/GetAssetType/$',asset_type_selector,name='asset_type_selector'),

    url(r'^Asset/Location/create/$', asset_create_location, name='asset_create_location'),
    url(r'^Asset/(?P<kvm>[\w\s]+)/Search/$', asset_search, name='asset_search'),

    url(r'^Asset/Machine/create/$', asset_create_machine, name='asset_create_machine'),
    url(r'^Asset/Tool/create/$', asset_create_tool, name='asset_create_tool'),
    url(r'^Asset/(?P<id>\d+)/delete/$', asset_delete, name='asset_delete'),
    url(r'^Asset/(?P<id>\d+)/gen_code$', gen_asset_code, name='gen_asset_code'),
    url(r'^Asset/(?P<id>\d+)/update/$', asset_update, name='asset_update'),
    url(r'^Asset/(?P<id>\d+)/listtree/$', show_asset_tree, name='show_asset_tree'),
    url(r'^Asset/(?P<woId>\d+)/listAssetWO/$', js_list_assetWo, name='js_list_assetWo'),
    url(r'^Asset/(?P<woId>\d+)/listAssetSWO/$', js_list_assetSWo, name='js_list_assetSWo'),
    url(r'^Asset/(?P<woId>\d+)/listAssetCloseWO/$', js_list_assetCloseWo, name='js_list_assetCloseWo'),
    url(r'^Asset/(?P<woId>\d+)/listAssetConsumedPart/$', js_list_assetConsumedPart, name='js_list_assetConsumedPart'),

    url(r'^Asset/Category/$', get_assetCategory, name='get_assetCategory'),
    url(r'^AssetCategory/$', list_assetCategory, name='list_assetCategory'),
    url(r'^AssetCategory/create/$', assetCategory_create, name='assetCategory_create'),
    url(r'^AssetCategory/(?P<id>\d+)/update/$', assetCategory_update, name='assetCategory_update'),
    url(r'^AssetCategory/(?P<id>\d+)/delete/$', assetCategory_delete, name='assetCategory_delete'),
    url(r'^Asset/Category2/$', get_assetCategoryMain, name='get_assetCategoryMain'),
    url(r'^Asset/Category2/(?P<ids>\d+(?:,\d+)*)$', get_assetCategoryMain, name='get_assetCategoryMain'),
    url(r'^Asset/Location/Category$', get_location_by_category, name='get_location_by_category'),
    url(r'^Asset/Clone/(?P<ids>\d+(?:,\d+)*)$', clone_asset, name='clone_asset'),
    url(r'^Asset/duplicate/(?P<id>\d+)$', duplicate_asset, name='duplicate_asset'),
    url(r'^Asset/BulkDelete/(?P<ids>\d+(?:,\d+)*)$', bulk_delete_asset, name='bulk_delete_asset'),
    url(r'^Asset/GetAssets$', asset_getAssets, name='asset_getAssets'),
    url(r'^Asset/Asset/create$', assetAsset_craete, name='assetAsset_craete'),
    url(r'^Asset/Asset/(?P<id>\d+)/listAssetAsset$', list_assetAsset, name='list_assetAsset'),
    url(r'^Asset/Asset/(?P<id>\d+)/delete/(?P<ch_id>\d+)$', assetAsset_delete, name='assetAsset_delete'),
    url(r'^AssetPart/$',list_assetPart,name='list_assetPart'),
    url(r'^AssetPart/create/$', assetPart_create, name='assetPart_create'),
    url(r'^AssetPart/(?P<id>\d+)/delete/$', assetPart_delete, name='assetPart_delete'),
    url(r'^AssetPart/(?P<id>\d+)/update/$', assetPart_update, name='assetPart_update'),
    url(r'^AssetPart/(?P<woId>\d+)/listAssetPart/$', js_list_assetPart, name='js_list_assetPart'),



     url(r'^Business/$',list_business,name='list_business'),
     url(r'^Business/Upload$',upload_business,name='upload_business'),
     url(r'^Business/Upload_File$',upload_file_business,name='upload_file_business'),
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
      url(r'^Part/Upload$',upload_part,name='upload_part'),
      url(r'^Part/Upload_File$',upload_file_part,name='upload_file_part'),
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
      url(r'^Purchase/ItemView/$', list_item_view, name='list_item_view'),
      url(r'^Purchase/Item/Change_Status/', change_purchase_item_status, name='change_purchase_item_status'),

      url(r'^Dashboard/Calendar/$', calendar, name='calendar'),
      url(r'^Dashboard/Profile/$', profile, name='profile'),
      url(r'^PurchaseReq/api/', PurchaseRequestList, name='PurchaseRequestList'),
      url(r'^Purchase/api/', PurchaseList2, name='PurchaseList2'),
      url(r'^Purchase/form/api', purchase_api_create, name='purchase_api_create'),
      path('api-token-auth/', obtain_auth_token, name='api_token_auth'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
