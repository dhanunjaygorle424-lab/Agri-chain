import random
from django.shortcuts import render, redirect
from django.contrib import messages
from buyers.models import (
    BuyerUserRegistrationModel,
    BuyerCropCartModels,
    BuyerTransactionModels,
    BlockChainTransactionModel,
    BuyerNotificationModel,
)
from buyers.forms import BuyerUserRegistrationForm
from sellers.models import FarmersCropsModels
from buyers.utility.BlockChainImpl import Blockchain


def index(request):
    return render(request, 'index.html')


def BuyerLogin(request):
    return render(request, 'BuyerLogin.html')


def BuyerRegister(request):
    form = BuyerUserRegistrationForm()
    return render(request, 'BuyerUserRegistrations.html', {'form': form})


def BuyerUserRegisterActions(request):
    if request.method == 'POST':
        form = BuyerUserRegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status = 'waiting'
            obj.save()
            messages.success(request, 'Registration successful! Please wait for admin activation.')
            return render(request, 'BuyerLogin.html')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
            return render(request, 'BuyerUserRegistrations.html', {'form': form})
    return redirect('BuyerRegister')


def BuyerUserLoginCheck(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        password = request.POST.get('password')
        try:
            buyer = BuyerUserRegistrationModel.objects.get(loginid=loginid, password=password)
            if buyer.status == 'activated':
                request.session['buyerloginid'] = buyer.loginid
                request.session['buyername'] = buyer.name
                request.session['buyeremail'] = buyer.email
                cart_count = BuyerCropCartModels.objects.filter(buyerusername=buyer.name, status='pending').count()
                notification_count = BuyerNotificationModel.objects.filter(buyer_username=buyer.name, is_read=False).count()
                return render(request, 'buyers/BuyerUserHome.html', {'buyer': buyer, 'cart_count': cart_count, 'notification_count': notification_count})
            else:
                messages.error(request, 'Your account is not activated yet. Please wait for admin approval.')
                return render(request, 'BuyerLogin.html')
        except BuyerUserRegistrationModel.DoesNotExist:
            messages.error(request, 'Invalid Login ID or Password.')
            return render(request, 'BuyerLogin.html')
    return redirect('BuyerLogin')


def BuyerUserHome(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyer = BuyerUserRegistrationModel.objects.get(loginid=loginid)
    cart_count = BuyerCropCartModels.objects.filter(buyerusername=buyer.name, status='pending').count()
    notification_count = BuyerNotificationModel.objects.filter(buyer_username=buyer.name, is_read=False).count()
    return render(request, 'buyers/BuyerUserHome.html', {'buyer': buyer, 'cart_count': cart_count, 'notification_count': notification_count})


def BuyerSearchProductsForm(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    return render(request, 'buyers/BuyerSearchProducts.html')


def BuyerSearchCropsAction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        crops = FarmersCropsModels.objects.filter(cropname__icontains=search)
        return render(request, 'buyers/BuyerSearchResults.html', {'crops': crops, 'search': search})
    return redirect('BuyerSearchProductsForm')


def BuyerAddCropsToCart(request):
    crop_id = request.GET.get('id')
    crop = FarmersCropsModels.objects.get(id=crop_id)
    buyername = request.session.get('buyername')
    buyeremail = request.session.get('buyeremail')

    BuyerCropCartModels.objects.create(
        buyerusername=buyername,
        buyeruseremail=buyeremail,
        sellername=crop.sellername,
        cropname=crop.cropname,
        description=crop.description,
        price=crop.price,
        file=crop.file,
        status='pending',
    )
    messages.success(request, f'{crop.cropname} added to cart!')
    crops = FarmersCropsModels.objects.all()
    return render(request, 'buyers/BuyerSearchResults.html', {'crops': crops, 'search': ''})


def BuyyerCheckCartData(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyername = request.session.get('buyername')
    carts = BuyerCropCartModels.objects.filter(buyerusername=buyername, status__in=['pending', 'approved', 'rejected'])
    approved_carts = [c for c in carts if c.status == 'approved']
    total = sum(c.price for c in approved_carts)
    return render(request, 'buyers/BuyerCheckInCart.html', {'carts': carts, 'total': total})


def BuyerDeleteanItemfromCart(request):
    cart_id = request.GET.get('id')
    BuyerCropCartModels.objects.filter(id=cart_id).delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('BuyyerCheckCartData')


def BuyerTotalAmountCheckOut(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyername = request.session.get('buyername')
    carts = BuyerCropCartModels.objects.filter(buyerusername=buyername, status='approved')
    total = sum(c.price for c in carts)
    if not carts:
        messages.error(request, 'No approved items to checkout. Please wait for seller approval.')
        return redirect('BuyyerCheckCartData')
    banks = ['State Bank of India', 'HDFC Bank', 'ICICI Bank', 'Axis Bank', 'Punjab National Bank',
             'Bank of Baroda', 'Canara Bank', 'Union Bank of India']
    selected_bank = random.choice(banks)
    return render(request, 'buyers/BuyerInitiateTransactionForm.html', {
        'carts': carts,
        'total': total,
        'bank': selected_bank,
    })


def StartBlockChainTransaction(request):
    if request.method == 'POST':
        buyername = request.session.get('buyername')
        totalamount = float(request.POST.get('totalamount'))
        recipientname = request.POST.get('recipientname')
        cardnumber = int(request.POST.get('cardnumber'))
        nameoncard = request.POST.get('nameoncard')
        cvv = int(request.POST.get('cvv'))
        cardexpiry = request.POST.get('cardexpiry')

        # Save transaction
        BuyerTransactionModels.objects.create(
            buyername=buyername,
            totalamount=totalamount,
            recipientname=recipientname,
            cradnumber=cardnumber,
            nameoncard=nameoncard,
            cvv=cvv,
            cardexpiry=cardexpiry,
        )

        # Create blockchain
        blockchain = Blockchain()
        blockchain.new_transaction(sender=buyername, recipient=recipientname, amount=str(totalamount))
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = last_proof + 1
        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof, previous_hash)

        # Save blockchain transaction to DB
        prev = blockchain.chain[-2] if len(blockchain.chain) > 1 else blockchain.chain[0]
        current = blockchain.chain[-1]

        p_trans = prev['transactions'][0] if prev['transactions'] else {'sender': 'Genesis', 'recipient': 'Genesis', 'amount': '0'}
        c_trans = current['transactions'][0] if current['transactions'] else {'sender': buyername, 'recipient': recipientname, 'amount': str(totalamount)}

        BlockChainTransactionModel.objects.create(
            c_index=str(current['index']),
            c_timestamp=str(current['timestamp']),
            c_sender=c_trans.get('sender', buyername),
            c_recipient=c_trans.get('recipient', recipientname),
            c_amount=c_trans.get('amount', str(totalamount)),
            c_proof=str(current['proof']),
            c_previous_hash=str(current['previous_hash']),
            p_index=str(prev['index']),
            p_timestamp=str(prev['timestamp']),
            p_sender=p_trans.get('sender', 'Genesis'),
            p_recipient=p_trans.get('recipient', 'Genesis'),
            p_amount=p_trans.get('amount', '0'),
            p_proof=str(prev['proof']),
            p_previous_hash=str(prev['previous_hash']),
        )

        # Update cart status
        carts = BuyerCropCartModels.objects.filter(buyerusername=buyername, status='approved')
        carts.update(status='purchased')

        return render(request, 'buyers/TransactionResults.html', {
            'block': current,
            'previous_block': prev,
            'chain': blockchain.chain,
            'totalamount': totalamount,
        })
    return redirect('BuyerUserHome')


def BuyerViewPurchasedDetails(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyername = request.session.get('buyername')
    purchased = BuyerCropCartModels.objects.filter(buyerusername=buyername, status='purchased')
    return render(request, 'buyers/BuyersViewPurchasedData.html', {'purchased': purchased})


def BuyerViewTransactinDetails(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyername = request.session.get('buyername')
    transactions = BuyerTransactionModels.objects.filter(buyername=buyername)
    return render(request, 'buyers/BuyersViewTransactionDetails.html', {'transactions': transactions})


def BuyerViewNotifications(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    buyername = request.session.get('buyername')
    notifications = BuyerNotificationModel.objects.filter(buyer_username=buyername).order_by('-created_at')
    return render(request, 'buyers/BuyerNotifications.html', {'notifications': notifications})


def BuyerMarkNotificationRead(request):
    loginid = request.session.get('buyerloginid')
    if not loginid:
        return redirect('BuyerLogin')
    notif_id = request.GET.get('id')
    BuyerNotificationModel.objects.filter(id=notif_id).update(is_read=True)
    messages.success(request, 'Notification marked as read.')
    return redirect('BuyerViewNotifications')
