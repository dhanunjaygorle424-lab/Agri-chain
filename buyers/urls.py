from django.urls import path
from buyers import views

urlpatterns = [
    path('BuyerUserRegisterActions/', views.BuyerUserRegisterActions, name='BuyerUserRegisterActions'),
    path('BuyerUserLoginCheck/', views.BuyerUserLoginCheck, name='BuyerUserLoginCheck'),
    path('BuyerUserHome/', views.BuyerUserHome, name='BuyerUserHome'),
    path('BuyerSearchProductsForm/', views.BuyerSearchProductsForm, name='BuyerSearchProductsForm'),
    path('BuyerSearchCropsAction/', views.BuyerSearchCropsAction, name='BuyerSearchCropsAction'),
    path('BuyerAddCropsToCart/', views.BuyerAddCropsToCart, name='BuyerAddCropsToCart'),
    path('BuyyerCheckCartData/', views.BuyyerCheckCartData, name='BuyyerCheckCartData'),
    path('BuyerDeleteanItemfromCart/', views.BuyerDeleteanItemfromCart, name='BuyerDeleteanItemfromCart'),
    path('BuyerTotalAmountCheckOut/', views.BuyerTotalAmountCheckOut, name='BuyerTotalAmountCheckOut'),
    path('StartBlockChainTransaction/', views.StartBlockChainTransaction, name='StartBlockChainTransaction'),
    path('BuyerViewPurchasedDetails/', views.BuyerViewPurchasedDetails, name='BuyerViewPurchasedDetails'),
    path('BuyerViewTransactinDetails/', views.BuyerViewTransactinDetails, name='BuyerViewTransactinDetails'),
    path('BuyerViewNotifications/', views.BuyerViewNotifications, name='BuyerViewNotifications'),
    path('BuyerMarkNotificationRead/', views.BuyerMarkNotificationRead, name='BuyerMarkNotificationRead'),
]
