from django.shortcuts import render, redirect
from django.contrib import messages
from sellers.models import SellerUserRegistrationModel, FarmersCropsModels
from sellers.forms import SellerUserRegistrationForm
from buyers.models import BuyerCropCartModels


def SellerLogin(request):
    return render(request, 'SellerLogin.html')


def SellerRegister(request):
    form = SellerUserRegistrationForm()
    return render(request, 'SellerUserRegistrations.html', {'form': form})


def SellerUserRegisterActions(request):
    if request.method == 'POST':
        form = SellerUserRegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status = 'waiting'
            obj.save()
            messages.success(request, 'Registration successful! Please wait for admin activation.')
            return render(request, 'SellerLogin.html')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
            return render(request, 'SellerUserRegistrations.html', {'form': form})
    return redirect('SellerRegister')


def SellerUserLoginCheck(request):
    if request.method == 'POST':
        loginid = request.POST.get('loginid')
        password = request.POST.get('password')
        try:
            seller = SellerUserRegistrationModel.objects.get(loginid=loginid, password=password)
            if seller.status == 'activated':
                request.session['sellerloginid'] = seller.loginid
                request.session['sellername'] = seller.name
                request.session['selleremail'] = seller.email
                return render(request, 'sellers/SellerUserHome.html', {'seller': seller})
            else:
                messages.error(request, 'Your account is not activated yet. Please wait for admin approval.')
                return render(request, 'SellerLogin.html')
        except SellerUserRegistrationModel.DoesNotExist:
            messages.error(request, 'Invalid Login ID or Password.')
            return render(request, 'SellerLogin.html')
    return redirect('SellerLogin')


def SellerUserHome(request):
    loginid = request.session.get('sellerloginid')
    if not loginid:
        return redirect('SellerLogin')
    seller = SellerUserRegistrationModel.objects.get(loginid=loginid)
    return render(request, 'sellers/SellerUserHome.html', {'seller': seller})


def SellerAddItemsForm(request):
    loginid = request.session.get('sellerloginid')
    if not loginid:
        return redirect('SellerLogin')
    return render(request, 'sellers/SellerAddItems.html')


def SellerAddItemsAction(request):
    if request.method == 'POST':
        sellername = request.session.get('sellername')
        selleremail = request.session.get('selleremail')
        cropname = request.POST.get('cropname')
        price = request.POST.get('price')
        description = request.POST.get('description')
        cropfile = request.FILES.get('file')

        FarmersCropsModels.objects.create(
            sellername=sellername,
            selleremail=selleremail,
            cropname=cropname,
            price=float(price),
            description=description,
            file=cropfile,
        )
        messages.success(request, 'Crop added successfully!')
        return render(request, 'sellers/SellerAddItems.html')
    return redirect('SellerAddItemsForm')


def SellersCommodities(request):
    loginid = request.session.get('sellerloginid')
    if not loginid:
        return redirect('SellerLogin')
    sellername = request.session.get('sellername')
    crops = FarmersCropsModels.objects.filter(sellername=sellername)
    return render(request, 'sellers/SellersCommoditiesData.html', {'crops': crops})


def SellerUpdateProducts(request):
    crop_id = request.GET.get('id')
    crop = FarmersCropsModels.objects.get(id=crop_id)
    return render(request, 'sellers/CropsUpdatesbySeller.html', {'crop': crop})


def SellerCropUpdateAction(request):
    if request.method == 'POST':
        crop_id = request.POST.get('id')
        crop = FarmersCropsModels.objects.get(id=crop_id)
        crop.cropname = request.POST.get('cropname')
        crop.price = float(request.POST.get('price'))
        crop.description = request.POST.get('description')
        if request.FILES.get('file'):
            crop.file = request.FILES.get('file')
        crop.save()
        messages.success(request, 'Crop updated successfully!')
        sellername = request.session.get('sellername')
        crops = FarmersCropsModels.objects.filter(sellername=sellername)
        return render(request, 'sellers/SellersCommoditiesData.html', {'crops': crops})
    return redirect('SellersCommodities')


def SellerDeleteProducts(request):
    crop_id = request.GET.get('id')
    FarmersCropsModels.objects.filter(id=crop_id).delete()
    messages.success(request, 'Crop deleted successfully!')
    sellername = request.session.get('sellername')
    crops = FarmersCropsModels.objects.filter(sellername=sellername)
    return render(request, 'sellers/SellersCommoditiesData.html', {'crops': crops})


def SellerViewCarts(request):
    loginid = request.session.get('sellerloginid')
    if not loginid:
        return redirect('SellerLogin')
    sellername = request.session.get('sellername')
    carts = BuyerCropCartModels.objects.filter(sellername=sellername)
    return render(request, 'sellers/SellersViewCart.html', {'carts': carts})
