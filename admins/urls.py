from django.urls import path
from admins import views

urlpatterns = [
    path('AdminLoginCheck/', views.AdminLoginCheck, name='AdminLoginCheck'),
    path('AdminHome/', views.AdminHome, name='AdminHome'),
    path('AdminActivateBuyers/', views.AdminActivateBuyers, name='AdminActivateBuyers'),
    path('AdminActivateBuyerAction/', views.AdminActivateBuyerAction, name='AdminActivateBuyerAction'),
    path('AdminActivateSellers/', views.AdminActivateSellers, name='AdminActivateSellers'),
    path('AdminActivateSellerAction/', views.AdminActivateSellerAction, name='AdminActivateSellerAction'),
    path('AdminViewBlockChainTransactions/', views.AdminViewBlockChainTransactions, name='AdminViewBlockChainTransactions'),
]
