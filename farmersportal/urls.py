from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from buyers import views as buyer_views
from sellers import views as seller_views
from admins import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', buyer_views.index, name='index'),
    path('SellerLogin/', seller_views.SellerLogin, name='SellerLogin'),
    path('BuyerLogin/', buyer_views.BuyerLogin, name='BuyerLogin'),
    path('AdminLogin/', admin_views.AdminLogin, name='AdminLogin'),
    path('SellerRegister/', seller_views.SellerRegister, name='SellerRegister'),
    path('BuyerRegister/', buyer_views.BuyerRegister, name='BuyerRegister'),
    path('sellers/', include('sellers.urls')),
    path('buyers/', include('buyers.urls')),
    path('admins/', include('admins.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
