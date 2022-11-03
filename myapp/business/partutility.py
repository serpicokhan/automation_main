from myapp.models.users import *
from myapp.models.parts import *
from django.db.models import Q
from django.core.paginator import *

class PartUtility:
    @staticmethod
    def getParts(searchStr):
        qstr=searchStr
        result=Part.objects.all()

        for q in searchStr:
            result = result.filter(Q(partName__icontains=qstr)|Q(partCode__icontains=qstr)|Q(partCategory__name__icontains=qstr)).order_by('-id').values('id', 'partName')
        # res= Part.objects.filter(partName__isnull=False).filter(partName__icontains=searchStr)
        result=result.extra(select={'length':'Length(partName)'}).order_by('length').values('id', 'partName','partCode')[:10]

        return result
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
