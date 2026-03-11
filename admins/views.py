from django.shortcuts import render, redirect
from django.contrib import messages
from buyers.models import BuyerUserRegistrationModel, BlockChainTransactionModel
from sellers.models import SellerUserRegistrationModel


def AdminLogin(request):
    return render(request, 'AdminLogin.html')


def AdminLoginCheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin123':
            request.session['adminlogin'] = True
            return render(request, 'admins/AdminHome.html')
        else:
            messages.error(request, 'Invalid admin credentials.')
            return render(request, 'AdminLogin.html')
    return redirect('AdminLogin')


def AdminHome(request):
    if not request.session.get('adminlogin'):
        return redirect('AdminLogin')
    return render(request, 'admins/AdminHome.html')


def AdminActivateBuyers(request):
    if not request.session.get('adminlogin'):
        return redirect('AdminLogin')
    buyers = BuyerUserRegistrationModel.objects.all()
    return render(request, 'admins/AdminActivateBuyers.html', {'buyers': buyers})


def AdminActivateBuyerAction(request):
    buyer_id = request.GET.get('id')
    status = request.GET.get('status')
    buyer = BuyerUserRegistrationModel.objects.get(id=buyer_id)
    buyer.status = status
    buyer.save()
    messages.success(request, f'Buyer {buyer.name} has been {status}.')
    buyers = BuyerUserRegistrationModel.objects.all()
    return render(request, 'admins/AdminActivateBuyers.html', {'buyers': buyers})


def AdminActivateSellers(request):
    if not request.session.get('adminlogin'):
        return redirect('AdminLogin')
    sellers = SellerUserRegistrationModel.objects.all()
    return render(request, 'admins/AdminActivateSellers.html', {'sellers': sellers})


def AdminActivateSellerAction(request):
    seller_id = request.GET.get('id')
    status = request.GET.get('status')
    seller = SellerUserRegistrationModel.objects.get(id=seller_id)
    seller.status = status
    seller.save()
    messages.success(request, f'Seller {seller.name} has been {status}.')
    sellers = SellerUserRegistrationModel.objects.all()
    return render(request, 'admins/AdminActivateSellers.html', {'sellers': sellers})


def AdminViewBlockChainTransactions(request):
    if not request.session.get('adminlogin'):
        return redirect('AdminLogin')
    transactions = BlockChainTransactionModel.objects.all()
    return render(request, 'admins/AdminViewBlockChainTransactions.html', {'transactions': transactions})
