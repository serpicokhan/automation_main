from django.db import models
from myapp.models import SysUser
from datetime import datetime
from django.utils.timezone import now
import jdatetime
class Message(models.Model):
    read=3
    unread=2
    MessageStatus=(
    (read,'read'),
    (unread,'unread')
    )
    Highest=1
    High=2
    Medium=3
    Low=4
    Lowest=5
    Priority=(
        (Highest,'خیلی زیاد'),
        (High,'زیاد'),
        (Medium,'متوسط'),
        (Low,'پایین'),
        (Lowest,'خیلی پایین'),
    )
    def getdate(self):
        if self.sentTime.date()==datetime.now():
            return "{}".format(self.datetime.time())
        else:
            return jdatetime.date.fromgregorian(date=self.sentTime)
    msgPririty=models.IntegerField("پیامهای سیستمی",choices=Priority,null=True,blank=True)
    messageStatus=models.IntegerField("وضعیت",choices=MessageStatus)
    sentTime=models.DateTimeField(auto_now_add=True)
    fromUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,related_name="fromuser",verbose_name="از:")
    toUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,related_name="touser",verbose_name="به:")
    subject=models.CharField("موضوع",max_length=200,blank=True,null=True)
    Message=models.TextField(null=True,blank=True)
    class Meta:
        db_table="message"

class MessageFile(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.woFile.name)
        return v[len(v)-1]
    def get_size(self):
        return " MB {0:.2f}".format(self.woFile.size/1048576)

    msgFile=models.FileField(upload_to='documents/',max_length=200)
    msgFileworkorder=models.ForeignKey(Message,on_delete=models.CASCADE,blank=True,null=True)
    msgFiledateAdded=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="messagefile"
