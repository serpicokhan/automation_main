from myapp.models.users import *
from myapp.models.parts import *
from django.db.models import Q
from django.core.paginator import *
import json

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
    @staticmethod
    def get_nodes(node,links):
        # print(node)
        d = {}
        d['text'] = str(node[2])
        d['href']="#"+d['text']
        d['tags']=str(node[1])
        children = PartUtility.get_children(node,links)
        if children:
            d['nodes'] = [PartUtility.get_nodes(child,links) for child in children]
        return d
    @staticmethod
    def get_children(node,links):
        #print(node[1],"))))))))))node")
        c=[x for x in links if x[0] == node[1]]
        return c
    @staticmethod
    def getCategory():
        a=PartCategory.objects.all()
        b=[]
        links=[]
        for item in a:
            b.append((item.isPartOf.id if item.isPartOf else -1,item.id,item.name))
        # print(b)
        # parents, children = zip(*b)
        # root_nodes = {x for x in parets if x not in children}
        # for node in root_nodes:
        #     links.append(('Root', node))

        tree = PartUtility.get_nodes((-2,-1,'همه'),b)
        return json.dumps(tree, indent=4)
