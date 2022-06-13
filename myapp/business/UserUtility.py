from myapp.models import SysUser
import jdatetime
import datetime
from django.core.paginator import *
class UserUtility:


    @staticmethod
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
   
    @staticmethod
    def is_manager(uid):
        user1=SysUser.objects.get(userId=uid)
        return (user1.userId.groups.filter(name= 'manager').exists())
    @staticmethod
    def get_user_list(request):
        users=SysUser.objects.values_list("fullName", "id")
        request.session['users'] = list(users)
        request.session['my_id']=request.user.id
