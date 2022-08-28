# Default import
from django.shortcuts import render
from django.http import Http404

# DRF import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Model, Serializer import
from .models import Certificate, Transaction
from .serializers import CertificateSerializer, TransactionSerializer

# drf_yasg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# 공급자 ID 값을 기준으로 등록된 거래 내역 조회
@api_view(['GET'])
def get_transaction_by_supplier(request, pk):
    queryset = Transaction.objects.filter(supplier=pk)
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data)

# 등록된 모든 거래 내역 조회
@api_view(['GET'])
def get_all_transaction_list(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 체결된 거래 내역 조회
@api_view(['GET'])
def get_approved_transaction_list(request):
    queryset = Transaction.objects.filter(supplier__isnull=False) & Transaction.objects.filter(buyer__isnull=False)
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 미체결된 거래 내역 조회
@api_view(['GET'])
def get_unapproved_transaction_list(request):
    queryset = Transaction.objects.filter(buyer__isnull=True)
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자가 구매한 거래 내역 조회
@api_view(['GET'])
def get_approved_transaction_by_user(request):
    user = request.user
    
    # 전력 공급자는 구매 불가
    if user.is_supplier:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
    
    queryset = Transaction.objects.filter(buyer=user)
    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method = 'POST',
    operation_id = '인증서 구매 API',
    operation_description = '인증서를 구매합니다.',
    request_body = openapi.Schema(
        '',
        type = openapi.TYPE_OBJECT,
        properties = {
            'transactionID': openapi.Schema('구매할 인증서 ID', type=openapi.TYPE_INTEGER)
        },
        required = ['transactionID']
    ),
    response = {
        200: openapi.Response(
            """
            """
        )
    }
)
@api_view(['POST'])
def approve_transaction(request):
    user = request.user
    
    if user.is_supplier:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
    
    transaction = Transaction.objects.get(pk=request.data['transactionID'])
    
    if transaction.buyer:
        return Response(
            {'detail': 'Already approved transaction.'},
            status = status.HTTP_400_BAD_REQUEST
        )
    else:
        transaction.buyer = user
        transaction.save()
        serializer = TransactionSerializer(transaction, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

class CertificateAPI(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Certificate.objects.get(pk=pk)
    #     except:
    #         raise Http404
        
    def get(self, request):
        queryset = Certificate.objects.all()
        serializer = CertificateSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
def get_my_confirmed_transactions(my: string)
Transaction에서 내가 판매 신청하고 승인된 거래 내역만 반환

def get_my_all_transacrtions(my: string)
Transaction에서 내가 판매 신청한 모든 거래 내역 반환

def get_confirmed_transactions_in_average_price_per_day
승인된 거래 내역에 대해 하루 평균 싯가 반환

def make_transaction
판매 등록

def get_balance
잔고 반환
'''
