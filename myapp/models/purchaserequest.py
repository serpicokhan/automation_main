from django.db import models
from datetime import datetime
from myapp.models.Asset import Asset
import jdatetime
import os
class PurchaseRequest(models.Model):
    def get_pstatus(self):
                 if(self.PurchaseRequestAssetNot==True):
                     return "<i class='fa fa-check'></i>								"
                 else:
                     return "<i class='fa fa-close'></i>"
    def getQTY(self):
        if(self.PurchaseRequestAssetQty):
            return self.PurchaseRequestAssetQty
        return self.PurchaseRequestAssetQtyNot

    def get_dateCreated_jalali(self):
        return jdatetime.date.fromgregorian(date=self.PurchaseRequestDateTo)
    def is_in_manager(self):
        return (self.PurchaseRequestRequestedUser.userId.groups.filter(name= 'manager').exists())


    PurchaseRequestPartName=models.ForeignKey("Part",on_delete=models.CASCADE,null=True,blank=True,related_name="RequestedPart",verbose_name="مشخصات قطعه")
    PurchaseRequestMoreInfo=models.CharField("اطلاعات بیشتر",max_length = 100,null=True,blank=True)
    PurchaseRequestAssetNotInInventory=models.CharField("ناموجود در انبار؟ اطلاعات بیشتری شرح دهید",max_length = 100,null=True,blank=True)
    #not in inventory qty
    PurchaseRequestAssetQty=models.FloatField("تعداد")
    PurchaseRequestAssetQtyNot=models.FloatField("کمیت",null=True,blank=True)
    PurchaseRequestAssetNot=models.BooleanField("در صورت عدم تهیه تولید دچار وقفه میشود",default=False)
    PurchaseRequestNotInList=models.BooleanField(default=False,null=True)




    # PurchaseRequestWO = models.ForeignKey('WorkOrder',on_delete=models.CASCADE,null=True,blank=True,related_name="ImpactedWO",verbose_name="درخواست مربوطه")
    PurchaseRequestAsset = models.ForeignKey('Asset',on_delete=models.CASCADE,null=True,blank=True,related_name="ImpactedAsset",verbose_name="تجهیز")
    PurchaseRequestAssetMakan = models.ForeignKey('Asset',on_delete=models.CASCADE,null=True,blank=True,related_name="ImpactedLocation")
    PurchaseRequestDateTo = models.DateField("مهلت تا تاریخ", auto_now_add=True)
    # PurchaseRequestDateFrom = models.DateField("تاریخ درخواست",blank=True,null=True)
    # PurchaseRequestDate2 = models.DateField("مهلت تا تاریخ",default=datetime.now, blank=True,null=True)
    settingTimestamp=models.DateTimeField(auto_now_add=True)

    PurchaseRequestAuthUser = models.ForeignKey('SysUser',on_delete=models.CASCADE,verbose_name="کاربر مجاز",null=True,blank=True,related_name="PurchaseRequestAuthUser")
    PurchaseRequestPurchase=models.ForeignKey('Purchase',on_delete=models.CASCADE,null=True,blank=True,related_name="purchase")
    def __str__(self):
        return self.id

    class Meta:
       db_table = "purchaserequest"

class Purchase(models.Model):
    Requested=1
    onHold=2
    Draft=3
    Assigned=4
    Open=5
    workInProgress=6
    closedComplete=7
    closedIncomplete=8
    waitingForPart=9
    invisible=-1
    Highest=1
    High=2
    Medium=3
    Low=4
    Lowest=5
    Status=(
         (Requested,'درخواست شده')  ,
         (onHold,'متوقف'),
         (Assigned,'تخصیص داده شده'),
         (Open,'باز'),
         (workInProgress,'در حال پیشرفت'),
         (closedComplete,'بسته شده کامل'),
         (closedIncomplete,'بسته شده، ناقص'),
         (waitingForPart,'در انتظار قطعه'),

     )
    PurchaseStatus=models.IntegerField("وضعیت درخواست", choices=Status,null=True,blank=True)
    PurchaseRequestedUser = models.ForeignKey('SysUser',on_delete=models.CASCADE,verbose_name="کاربر درخواست کننده",null=True,related_name="PurchaseRequestdUser")
    PurchaseTayeedUser = models.ForeignKey('SysUser',on_delete=models.CASCADE,verbose_name="کاربر تایید کننده",null=True,blank=True,related_name="PurchaseAdmitter")
    PurchaseDateTo = models.DateField("تاریخ ", auto_now_add=True)
    PurchaseCompletionDate = models.DateField("تاریخ تکمیل",blank=True,null=True)



    class Meta:
       db_table = "purchase"

class RequestFile(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.woFile.name)
        return v[len(v)-1]
    def get_name(self):
        return os.path.basename(str(self.msgFile))
    def get_size(self):
        return " MB {0:.2f}".format(self.woFile.size/1048576)

    msgFile=models.FileField(upload_to='documents/%Y/%m/%d',max_length=200)
    msgFileworkorder=models.ForeignKey(Purchase,on_delete=models.CASCADE,blank=True,null=True)
    msgFiledateAdded=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="purchasefile"
class RequestVoice(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.woFile.name)
        return v[len(v)-1]
    def get_name(self):
        return os.path.basename(str(self.msgFile))
    def get_size(self):
        return " MB {0:.2f}".format(self.woFile.size/1048576)

    msgFile=models.FileField(upload_to='documents/%Y/%m/%d',max_length=200)
    msgFileworkorder=models.ForeignKey(Purchase,on_delete=models.CASCADE,blank=True,null=True)
    msgFiledateAdded=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="requestvoice"
