from rest_framework import generics
from myapp.models import PurchaseRequest,Purchase
from myapp.business.serializer import *
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def PurchaseRequestList(request):
    # queryset = PurchaseRequest.objects.all()
    # serializer_class = PurchaseRequestSerializer
    if request.method == 'GET':
        # print("!23")
        posts = PurchaseRequest.objects.all()
        serializer = PurchaseRequestSerializer(posts, many=True)
        # for k in serializer.data:
        #     # k.datecreated=DateJob.getDate2(k.datecreated)
        #     k["datecreated"]= str(jdatetime.datetime.fromgregorian(date=datetime.datetime.strptime(k["datecreated"], "%Y-%m-%d").date()).date()).replace('-','/')
        return Response(serializer.data)
@api_view(['GET'])
def PurchaseList2(request):
    # queryset = PurchaseRequest.objects.all()
    # serializer_class = PurchaseRequestSerializer
    if request.method == 'GET':
        # print("!23")
        posts = Purchase.objects.all()
        serializer = PurchaseSerializer(posts, many=True)
        # for k in serializer.data:
        #     # k.datecreated=DateJob.getDate2(k.datecreated)
        #     k["datecreated"]= str(jdatetime.datetime.fromgregorian(date=datetime.datetime.strptime(k["datecreated"], "%Y-%m-%d").date()).date()).replace('-','/')
        return Response(serializer.data)
@api_view(['POST'])
def purchase_api_create(request):
    serializer = PurchaseSerializerMini(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
