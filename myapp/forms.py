from django import forms
from myapp.models import *
from django.conf import settings
import logging
from django.forms import ModelForm, inlineformset_factory
from myapp.business.DateJob import *


class CopyAssetForm(forms.Form):
    assetname2= forms.ModelChoiceField(label="نام دستگاه",queryset=Asset.objects.all(),
    widget=forms.Select(attrs={'class':'selectpicker','data-live-search':'true','multiple':''}))


class AssetForm(forms.ModelForm):
    assetDescription = forms.CharField( label="توضیحات",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}),required=False )
    assetIsLocatedAt = forms.ModelChoiceField(label="مکان",queryset=Asset.objects.filter(assetTypes=1,assetIsLocatedAt__isnull=True),
    widget=forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}),required=False)
    # def clean_assetCategory(self):
    #     last_name = self.cleaned_data['assetCategory']
    #     print(last_name,"$$$$$$$$$$$$$$$$")
    #     return int(last_name)
    asseccategorytxt = forms.CharField(label='دسته بندی',required=False,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    assetispart = forms.CharField(label='دسته بندی',required=False,widget=forms.TextInput(attrs={'autocomplete':'off'}))

    class Meta:
        model = Asset
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        super(AssetForm, self).__init__(*args, **kwargs)
        # self.fields['assetCategory'].queryset = AssetCategory.objects.filter(id__lte=3)
# class AssetSubForm(forms.Form):
#     assetDescription = forms.CharField( label="توضیحات",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}),required=False )
#     # def clean_assetCategory(self):
#     #     last_name = self.cleaned_data['assetCategory']
#     #     print(last_name,"$$$$$$$$$$$$$$$$")
#     #     return int(last_name)
#     # asseccategorytxt = forms.CharField(label='دسته بندی',required=False,widget=forms.TextInput(attrs={'autocomplete':'off'}))
#             makan= forms.ModelChoiceField(label="نام مکان",queryset=Asset.objects.filter(assetIsLocatedAt__isnull=True),
#             widget=forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}))

class AssetPartForm(forms.ModelForm):
    mypart=forms.CharField(required=False)

    def clean(self):
                 self.is_valid()
                 cleaned_data=super(AssetPartForm, self).clean()
                 assetPartAssetid=cleaned_data.get('assetPartAssetid','')
                 assetPartPid=cleaned_data.get('assetPartPid','')
                 assetPartQnty=cleaned_data.get('assetPartQnty','')
                 assetPartDescription=cleaned_data.get('assetPartDescription','')



                 return cleaned_data
    class Meta:
        model = AssetPart
        fields = '__all__'
class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = '__all__'
class MiniBusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name', 'code', 'primaryContact']
class AssetCategoryForm(forms.ModelForm):

    class Meta:
        model = AssetCategory
        fields = '__all__'
class BusinessPartForm(forms.ModelForm):
    mypart = forms.CharField(label="نام قطعه",required=False,widget=forms.TextInput())

    def clean(self):
                self.is_valid()
                cleaned_data=super(BusinessPartForm, self).clean()
                BusinessPartPart=cleaned_data.get('BusinessPartPart','')
                businessPartBusiness=cleaned_data.get('businessPartBusiness','')
                businessPartBusinessType=cleaned_data.get('businessPartBusinessType','')
                businessPartSupplierPartNumber=cleaned_data.get('businessPartSupplierPartNumber','')
                businessPartCatalog=cleaned_data.get('businessPartCatalog','')
                businessPartisDefault=cleaned_data.get('businessPartisDefault','')

                return cleaned_data


    class Meta:
         model = BusinessPart
         fields = '__all__'
class BusinessAssetForm(forms.ModelForm):

    def clean(self):


                self.is_valid()
                cleaned_data=super(BusinessAssetForm, self).clean()
                BusinessAssetAsset=cleaned_data.get('BusinessAssetAsset','')
                businessAssetBusiness=cleaned_data.get('businessAssetBusiness','')
                businessAssetBusinessType=cleaned_data.get('businessAssetBusinessType','')
                businessAssetSupplierPartNumber=cleaned_data.get('businessAssetSupplierPartNumber','')
                businessAssetCatalog=cleaned_data.get('businessAssetCatalog','')
                businessAssetisDefault=cleaned_data.get('businessAssetisDefault','')

                return cleaned_data


    class Meta:
         model = BusinessAsset
         fields = '__all__'
class BusinessFileForm(forms.ModelForm):







    class Meta:
         model = BusinessFile
         fields = ('businessFile',)

class SysUserForm(forms.ModelForm):
    #CustomerId = forms.ModelChoiceField(queryset=Customer.objects.all())



    class Meta:
        model = SysUser
        fields = '__all__'
class MessageForm(forms.ModelForm):
    toUser = forms.ModelChoiceField(label="مخاطب",queryset=SysUser.objects.all(),empty_label='به کی')
    def clean_messageStatus(self):
        if(self.isupdated):
            messageStatus=3
        else:
            messageStatus=2

        return messageStatus



    class Meta:
        model = Message
        fields = '__all__'
class PurchaseForm(forms.ModelForm):
    # def clean_PurchaseDateTo(self):
    #     if(self.cleaned_data['PurchaseDateTo']):
    #          # print(self.cleaned_data['PurchaseRequestDateTo'],'datecompleted')
    #          value=DateJob.getDate2( self.cleaned_data['PurchaseDateTo'])
    #          return value
    #     else:
    #         return None
    # def clean_PurchaseDateFrom(self):
    #     if(self.cleaned_data['PurchaseDateFrom']):
    #          # print(self.cleaned_data['PurchaseRequestDateTo'],'datecompleted')
    #          value=DateJob.getDate2( self.cleaned_data['PurchaseDateFrom'])
    #          return value
    #     else:
    #         return None
    # toUser = forms.ModelChoiceField(label="مخاطب",queryset=SysUser.objects.all(),empty_label='به کی')




    class Meta:
        model = Purchase
        fields = '__all__'

class PurchaseRequestForm(forms.ModelForm):
    # def __init__(self,userid=None,*args,**kwargs):
    #
    #     super (PurchaseRequestForm,self ).__init__(*args,**kwargs) # populates the post
    #     try:
    #         self.fields['PurchaseRequestAsset'].queryset=Asset.objects.none()
    #         # print(self.data)
    #         if 'PurchaseRequestAssetMakan' in self.data:
    #                 try:
    #                     country_id = int(self.data.get('PurchaseRequestAssetMakan'))
    #                     self.fields['PurchaseRequestAsset'].queryset = Asset.objects.filter(assetIsLocatedAt=country_id).order_by('-id')
    #                 except (ValueError, TypeError):
    #                     pass  # invalid input from the client; ignore and fallback to empty City queryset
    #         elif self.instance.pk:
    #                 self.fields['PurchaseRequestAsset'].queryset = Asset.objects.filter(assetIsLocatedAt=self.instance.PurchaseRequestAssetMakan)
    #
    #
    #         # if(userid):
    #         #     user=SysUser.objects.get(userId=userid)
    #         #     print(user)
    #         #     if(user.userId.username =="admin"):
    #         #         print("not admin")
    #         #         self.fields['PurchaseRequestRequestedUser'].queryset = SysUser.objects.filter(userStatus=True)#books #AssetMeterTemplate.objects.filter(assetMeterTemplateAsset=WorkOrder.objects.get(id=workorder).woAsset)
    #         #     else:
    #         #         print(" is admin")
    #         #         self.fields['PurchaseRequestRequestedUser'].queryset = SysUser.objects.filter(userId=userid)
    #         #
    #         # else:
    #         #     self.fields['PurchaseRequestRequestedUser'].queryset = SysUser.objects.none()
    #     except Exception as ex:
    #         print(ex)
    mypart=forms.CharField(required=False)
    mysupplier=forms.CharField(required=False)
    PurchaseRequestAssetMakan= forms.ModelChoiceField(label="نام مکان",required=False,queryset=Asset.objects.filter(assetIsLocatedAt__isnull=True,assetTypes=1),
    widget=forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}))
    # PurchaseRequestAssetMakan= forms.ModelChoiceField(label="نام مکان",required=False,queryset=Asset.objects.filter(assetIsLocatedAt__isnull=True,assetTypes=1),
    # widget=forms.Select(attrs={'class':'selectpicker','data-live-search':'true'}))
    # PurchaseRequestAsset= forms.ModelChoiceField(required=False,label="دارایی ",queryset=Asset.objects.all(),
    # widget=forms.Select())
    # PurchaseRequestAssetNotInInventory = forms.CharField( label="ناموجود در انبار؟ اطلاعات بیشتری شرح دهید",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}),required=False )
    PurchaseRequestMoreInfo = forms.CharField( label="اطلاعات بیشتر",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}),required=False )
    #
    # def clean_PurchaseRequestDateTo(self):
    #     if(self.cleaned_data['PurchaseRequestDateTo']):
    #          # print(self.cleaned_data['PurchaseRequestDateTo'],'datecompleted')
    #          value=DateJob.getDate2( self.cleaned_data['PurchaseRequestDateTo'])
    #          return value
    #     else:
    #         return None
    # def clean_PurchaseRequestPartName(self):
    #      value=self.cleaned_data['PurchaseRequestPartName'][0]
    #      return value


    def clean_PurchaseRequestDateFrom(self):
        if(self.cleaned_data['PurchaseRequestDateFrom']):
             # print(self.cleaned_data['PurchaseRequestDateTo'],'datecompleted')
             value=DateJob.getDate2( self.cleaned_data['PurchaseRequestDateFrom'])
             return value
        else:
            return None

    class Meta:
        model = PurchaseRequest
        exclude = ('PurchaseRequestNotInList',)
###########################################################################
class PartForm(forms.ModelForm):
    partcategorytxt = forms.CharField(label='دسته بندی',required=False,widget=forms.TextInput(attrs={'autocomplete':'off'}))
    partDescription = forms.CharField( label="توضیحات",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}),required=False )

    class Meta:
        model = Part
        fields = '__all__'
###############################################################
class PartCategoryForm(forms.ModelForm):

    class Meta:
        model = PartCategory
        fields = '__all__'
