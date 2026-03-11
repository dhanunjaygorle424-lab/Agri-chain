from django.urls import path
from sellers import views

urlpatterns = [
    path('SellerUserRegisterActions/', views.SellerUserRegisterActions, name='SellerUserRegisterActions'),
    path('SellerUserLoginCheck/', views.SellerUserLoginCheck, name='SellerUserLoginCheck'),
    path('SellerUserHome/', views.SellerUserHome, name='SellerUserHome'),
    path('SellerAddItemsForm/', views.SellerAddItemsForm, name='SellerAddItemsForm'),
    path('SellerAddItemsAction/', views.SellerAddItemsAction, name='SellerAddItemsAction'),
    path('SellersCommodities/', views.SellersCommodities, name='SellersCommodities'),
    path('SellerUpdateProducts/', views.SellerUpdateProducts, name='SellerUpdateProducts'),
    path('SellerCropUpdateAction/', views.SellerCropUpdateAction, name='SellerCropUpdateAction'),
    path('SellerDeleteProducts/', views.SellerDeleteProducts, name='SellerDeleteProducts'),
    path('SellerViewCarts/', views.SellerViewCarts, name='SellerViewCarts'),
]
