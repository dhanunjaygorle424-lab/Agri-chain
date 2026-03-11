# Blockchain Farmers Portal — Build Spec

## Overview
Django web application — "Study of Blockchain Technology in Farmer's Portal"
A blockchain-based e-commerce portal for farmers to sell crops and buyers to purchase them, with all transactions recorded on a blockchain.

## Tech Stack
- Python 3 / Django
- SQLite database
- HTML/CSS/JS frontend (Bootstrap-based template with static assets)
- Custom blockchain implementation (SHA-256 hashing)

## Modules
1. **Sellers** — Register, login, add/update/delete crops with images
2. **Buyers** — Register, login, search crops, add to cart, purchase with blockchain transaction
3. **Admin** — Login, activate sellers/buyers, view blockchain transactions
4. **Blockchain** — Custom implementation recording purchase transactions

## Project Structure
```
blockchain-farmers-portal/
├── manage.py
├── farmersportal/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── buyers/                 # Buyer app
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── utility/
│       └── BlockChainImpl.py
├── sellers/                # Seller app
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── admins/                 # Admin app (custom, not Django admin)
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
├── templates/              # All HTML templates
│   ├── base.html
│   ├── index.html
│   ├── SellerLogin.html
│   ├── BuyerLogin.html
│   ├── AdminLogin.html
│   ├── SellerUserRegistrations.html
│   ├── BuyerUserRegistrations.html
│   ├── sellers/
│   │   ├── SellerUserHome.html
│   │   ├── SellerAddItems.html
│   │   ├── SellersCommoditiesData.html
│   │   ├── CropsUpdatesbySeller.html
│   │   └── SellersViewCart.html
│   ├── buyers/
│   │   ├── BuyerUserHome.html
│   │   ├── BuyerSearchProducts.html
│   │   ├── BuyerSearchResults.html
│   │   ├── BuyerCheckInCart.html
│   │   ├── BuyerInitiateTransactionForm.html
│   │   ├── TransactionResults.html
│   │   ├── BuyersViewPurchasedData.html
│   │   └── BuyersViewTransactionDetails.html
│   └── admins/
│       ├── AdminHome.html
│       ├── AdminViewBlockChainTransactions.html
│       ├── AdminActivateBuyers.html
│       └── AdminActivateSellers.html
├── static/                 # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
└── media/                  # Uploaded files
```

## Models

### Buyer Models (buyers/models.py)

```python
from django.db import models

class BuyerUserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'BuyersRegistrations'


class BuyerCropCartModels(models.Model):
    buyerusername = models.CharField(max_length=100)
    buyeruseremail = models.CharField(max_length=100)
    sellername = models.CharField(max_length=100)
    cropname = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    price = models.FloatField()
    file = models.FileField(upload_to='files/')
    cdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.buyerusername

    class Meta:
        db_table = "BuyerCartTable"


class BuyerTransactionModels(models.Model):
    buyername = models.CharField(max_length=100)
    totalamount = models.FloatField()
    recipientname = models.CharField(max_length=100)
    cradnumber = models.IntegerField()
    nameoncard = models.CharField(max_length=100)
    cvv = models.IntegerField()
    cardexpiry = models.CharField(max_length=200)
    trnx_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.buyername

    class Meta:
        db_table = "BuyerTransactionTable"

class BlockChainTransactionModel(models.Model):
    c_index = models.CharField(max_length=100)
    c_timestamp = models.CharField(max_length=100)
    c_sender = models.CharField(max_length=100)
    c_recipient = models.CharField(max_length=100)
    c_amount = models.CharField(max_length=100)
    c_proof = models.CharField(max_length=100)
    c_previous_hash = models.CharField(max_length=100)
    p_index = models.CharField(max_length=100)
    p_timestamp = models.CharField(max_length=100)
    p_sender = models.CharField(max_length=100)
    p_recipient = models.CharField(max_length=100)
    p_amount = models.CharField(max_length=100)
    p_proof = models.CharField(max_length=100)
    p_previous_hash = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "BlockChainTransactiontable"
```

### Seller Models (sellers/models.py)

```python
from django.db import models

class SellerUserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'SellerRegistrations'

class FarmersCropsModels(models.Model):
    sellername = models.CharField(max_length=100)
    selleremail = models.CharField(max_length=100)
    cropname = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100000)
    file = models.FileField(upload_to='files/')
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cropname

    class Meta:
        db_table = "FarmersCrops"
```

## Blockchain Implementation (buyers/utility/BlockChainImpl.py)

```python
import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="The Times 03/Oct/2020 A Study of Blockchain Technology in Farmer's Portal.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
```

## Views

### Buyer Views (buyers/views.py)
- BuyerUserRegisterActions — registration form handling
- BuyerUserLoginCheck — login with activation check
- BuyerUserHome — home page with cart count
- BuyerSearchProductsForm — search form
- BuyerSearchCropsAction — search results (icontains filter)
- BuyerAddCropsToCart — add crop to cart
- BuyyerCheckCartData — view cart items
- BuyerDeleteanItemfromCart — remove from cart
- BuyerTotalAmountCheckOut — checkout with random bank assignment
- StartBlockChainTransaction — process payment, create blockchain block, record transaction
- BuyerViewPurchasedDetails — view purchased items
- BuyerViewTransactinDetails — view transaction history

### Seller Views (sellers/views.py)
- SellerUserRegisterActions — registration
- SellerUserLoginCheck — login with activation check
- SellerUserHome — home page
- SellerAddItemsForm / SellerAddItemsAction — add crops with image upload
- SellersCommodities — view own crops
- SellerUpdateProducts / SellerCropUpdateAction — update crops
- SellerDeleteProducts — delete crops
- SellerViewCarts — view buyer cart items for this seller

### Admin Views (admins/views.py)
- AdminLoginCheck — admin login (hardcoded admin/admin123)
- AdminHome — admin home page
- AdminActivateBuyers / AdminActivateBuyerAction — list and activate buyers
- AdminActivateSellers / AdminActivateSellerAction — list and activate sellers
- AdminViewBlockChainTransactions — view all blockchain transactions

## Forms
### BuyerUserRegistrationForm — ModelForm for BuyerUserRegistrationModel (status defaults to 'waiting')
### SellerUserRegistrationForm — ModelForm for SellerUserRegistrationModel (status defaults to 'waiting')

## URL Patterns
- / — index (home page)
- /SellerLogin/ — seller login page
- /BuyerLogin/ — buyer login page  
- /AdminLogin/ — admin login page
- /SellerRegister/ — seller registration
- /BuyerRegister/ — buyer registration
- /sellers/ — seller app URLs
- /buyers/ — buyer app URLs
- /admins/ — admin app URLs

## Templates
Use Bootstrap-based theme. base.html has navbar with links to Home, Seller, Buyer, Admin, SellerRegister, BuyerRegister.
All templates extend base.html. For static files, use CDN-based Bootstrap + Font Awesome instead of local static files to avoid needing the original theme assets.

## Admin Credentials
- Username: admin
- Password: admin123

## Important Notes
1. The `status` field for buyers/sellers defaults to 'waiting' — admin must activate
2. Blockchain is in-memory (resets on server restart) but transactions are also saved to DB
3. File uploads (crop images) go to media/files/
4. Card payment is simulated (no real payment gateway)
5. Make all templates functional with clean Bootstrap UI
6. Use CDN for CSS/JS (Bootstrap 4, Font Awesome) — don't rely on local static theme files
