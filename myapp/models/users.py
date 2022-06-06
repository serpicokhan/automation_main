#python manage.py makemigrations
#After that you just have to run migrate command for syncing database .

#python manage.py migrate --run-syncdb
from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User
import jdatetime
from django.utils.timezone import now
# from cmms.models.Asset import *
class testuser(models.Model):
    # password=models.CharField(max_length=20)
    massage=models.CharField("مشخصات کامل",max_length = 50)
    class Meta:
        db_table="testuser"


class SysUser(models.Model):
    def __str__(self):
        return "{}".format(self.fullName)
    def get_userStatus(self):
                 if(self.userStatus==True):
                     return "<i class='fa fa-play'></i>								"
                 else:
                     return "<i class='fa fa-stop'></i>"
    def getName(self):

        xxxx=UserGroups.objects.filter(userUserGroups=self.id)
        st=[]
        for i in xxxx:
            st.append(i.groupUserGroups)
        # print(''.join(str(e) for e in st))
        return '<br/>'.join(str(e) for e in st)


    Dashboard=1
    WorkOrderAssignedToMe=2
    MessageCenterInbox=3
    WorkOrders=4
    Location=(
        (Dashboard,'داشبورد'),
        (WorkOrderAssignedToMe,'درخواستهای انتسابی به من'),
        (MessageCenterInbox,'صندوق ورودی پیامها'),
        (WorkOrders,'درخواست'),
    )
    userId = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    password=models.CharField(max_length=20)
    token=models.CharField(max_length=20,null=True,blank=True)
    fullName=models.CharField("مشخصات کامل",max_length = 50)
    personalCode=models.CharField("کد پرسنلی",max_length = 50)
    title=models.CharField("نام کاربری",max_length = 50,null=True,blank=True)
    email=models.EmailField("ایمیل",max_length=70,blank=True, null= True, unique= True)
    profileImage = models.ImageField(upload_to='images/',default=None,blank=True)

    userStatus=models.BooleanField("وضعیت",default=True)

    class Meta:
        db_table="sysusers"
        ordering = ['title']



class UserGroup(models.Model):
    def __str__(self):
        if(self.userUserLocation):
            return "{}:{}".format(self.userGroupName,self.userUserLocation)
        else:
            return "{}".format(self.userGroupName)

    userGroupCode=models.CharField("کد",max_length=50)
    userGroupName=models.CharField("نام",max_length=50)

    userGroupIsPartOF=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,verbose_name='زیرمجموعه')

    class Meta:
        db_table="usergroup"

class UserGroups(models.Model):


    userUserGroups=models.ForeignKey(SysUser,on_delete=models.CASCADE,blank=True,null=True)
    groupUserGroups=models.ForeignKey(UserGroup,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        db_table="usergroups"
class UserFile(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.userFile.name)
        return v[len(v)-1]
    def get_size(self):
        return " MB {0:.2f}".format(self.userFile.size/1048576)

    userFile=models.FileField(upload_to='documents/')
    userFileUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,blank=True,null=True)
    userFiledateAdded=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="userfile"

