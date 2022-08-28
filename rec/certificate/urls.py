from django.urls import path
from . import views

urlpatterns = [
    # 거래 내역 조회
    path('transaction/list/<int:pk>', views.get_transaction_by_supplier),
    path('transaction/list/', views.get_all_transaction_list),
    
    # 승인된 거래 내역 조회
    path('transaction/approved/', views.get_approved_transaction_list),
    path('transaction/approved/by-user/', views.get_approved_transaction_by_user),
    
    # 미승인된 거래 내역 조회
    path('transaction/unapproved/', views.get_unapproved_transaction_list),
    
    # 인증서 거래
    path('transaction/approve/', views.approve_transaction),
]
