#!/usr/bin/env python3
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmersportal.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from sellers.models import SellerUserRegistrationModel, FarmersCropsModels
from buyers.models import BuyerUserRegistrationModel, BuyerCropCartModels, BuyerTransactionModels, BlockChainTransactionModel

# --- Seller Registrations ---
sellers = [
    {"name": "alex", "loginid": "alex", "password": "Alex@141", "mobile": "9849098490", "email": "lx160cm@gmail.com", "locality": "East Streets", "address": "#303, East Streets", "city": "Hyderabad", "state": "Telangana", "status": "activated"},
    {"name": "Sagar", "loginid": "sagar", "password": "Sagarbabu@141", "mobile": "9700596968", "email": "marrisagar21@gmail.com", "locality": "madinaguda", "address": "#302, madinaguda", "city": "Godavarikhani", "state": "Telangana", "status": "activated"},
    {"name": "sravani", "loginid": "sravani", "password": "Sravani@141", "mobile": "9849012345", "email": "sravanisravs@gmail.com", "locality": "Noida", "address": "#303, Noida", "city": "Warangal", "state": "Telangana", "status": "activated"},
    {"name": "adnan", "loginid": "adnan", "password": "Adnan123", "mobile": "9701319983", "email": "adnanuddin@gmail.com", "locality": "abcd", "address": "abcd", "city": "hyderabad", "state": "telangana", "status": "activated"},
    {"name": "aaa", "loginid": "aaa", "password": "Seller@123", "mobile": "9700493122", "email": "mohdabdulhaseeb18@gmail.com", "locality": "hyd", "address": "hyd", "city": "hyd", "state": "ts", "status": "activated"},
    {"name": "faisal", "loginid": "faisal", "password": "Faisal@123", "mobile": "9700456789", "email": "faisal@gmail.com", "locality": "abcd", "address": "abcd", "city": "hyderBAD", "state": "telangana", "status": "activated"},
]

for s in sellers:
    obj, created = SellerUserRegistrationModel.objects.get_or_create(loginid=s["loginid"], defaults=s)
    print(f"Seller '{s['loginid']}': {'created' if created else 'exists'}")

# --- Buyer Registrations ---
buyers = [
    {"name": "Meghana", "loginid": "meghana", "password": "Meghana@141", "mobile": "9566089897", "email": "arumallameghana@gmail.com", "locality": "Moulana Steets", "address": "#201, Moulana Steets", "city": "Vijayawada", "state": "Andhrapradesh", "status": "activated"},
    {"name": "Harish", "loginid": "harish", "password": "Harish@141", "mobile": "9568878789", "email": "harishgangishetty@gmail.com", "locality": "New", "address": "#303 New", "city": "Markapuram", "state": "Andhrapradesh", "status": "activated"},
    {"name": "Ramesh", "loginid": "ramesh", "password": "Ramesh@141", "mobile": "9849045458", "email": "rameshsrc@gmail.com", "locality": "Vakilpally", "address": "# new Vakilpally Flots, 10-25, Centanary Colony", "city": "Hyderabd", "state": "Telangana", "status": "activated"},
    {"name": "haseeb", "loginid": "haseeb", "password": "Haseeb123", "mobile": "9700493122", "email": "mohdabdulhaseeb@gmail.com", "locality": "Abcd", "address": "Abcd", "city": "Hyderabad", "state": "Telangana", "status": "activated"},
    {"name": "bbb", "loginid": "bbb", "password": "Buyer@123", "mobile": "9701319983", "email": "adnanuddin@gmail.com", "locality": "abcd", "address": "abcd", "city": "hyderabad", "state": "telangana", "status": "activated"},
]

for b in buyers:
    obj, created = BuyerUserRegistrationModel.objects.get_or_create(loginid=b["loginid"], defaults=b)
    print(f"Buyer '{b['loginid']}': {'created' if created else 'exists'}")

# --- Farmer Crops ---
crops = [
    {"sellername": "alex", "selleremail": "lx160cm@gmail.com", "cropname": "Tomato", "price": 25.0, "description": "A red Tomato For Health"},
    {"sellername": "alex", "selleremail": "lx160cm@gmail.com", "cropname": "Green Beans", "price": 95.0, "description": "Healthy Diet"},
    {"sellername": "alex", "selleremail": "lx160cm@gmail.com", "cropname": "STRAWBERRY", "price": 150.0, "description": "A great Choice if you have"},
    {"sellername": "sagar", "selleremail": "marrisagar21@gmail.com", "cropname": "BROCOLLI", "price": 250.0, "description": "A new Choice To Digest"},
    {"sellername": "sagar", "selleremail": "marrisagar21@gmail.com", "cropname": "CARROTS", "price": 89.9, "description": "Best For Health"},
    {"sellername": "sravani", "selleremail": "sravanisravs@gmail.com", "cropname": "Onion", "price": 35.0, "description": "A Maharstra onion"},
    {"sellername": "adnan", "selleremail": "adnanuddin@gmail.com", "cropname": "Apple", "price": 100.0, "description": "100% Natural"},
    {"sellername": "aaa", "selleremail": "mohdabdulhaseeb18@gmail.com", "cropname": "Apple", "price": 100.0, "description": "100% Natural"},
]

for c in crops:
    obj = FarmersCropsModels.objects.create(**c)
    print(f"Crop '{c['cropname']}' by {c['sellername']}: created (id={obj.id})")

# --- Buyer Transactions ---
transactions = [
    {"buyername": "harish", "totalamount": 50.0, "recipientname": "HDFC Bank", "cradnumber": 2500458096963652, "nameoncard": "Harish Gangishetti", "cvv": 645, "cardexpiry": "2022-12"},
    {"buyername": "harish", "totalamount": 300.0, "recipientname": "HDFC Bank", "cradnumber": 2512898965653214, "nameoncard": "Rashna", "cvv": 256, "cardexpiry": "2029-01"},
    {"buyername": "ramesh", "totalamount": 495.0, "recipientname": "Canara Bank", "cradnumber": 4589100250026001, "nameoncard": "Arumalla kattamma", "cvv": 568, "cardexpiry": "2022-12"},
    {"buyername": "ramesh", "totalamount": 25.0, "recipientname": "Canara Bank", "cradnumber": 2500787895951001, "nameoncard": "Suresh", "cvv": 256, "cardexpiry": "2021-12"},
    {"buyername": "meghana", "totalamount": 534.9, "recipientname": "SBI Bank", "cradnumber": 2560123489892525, "nameoncard": "Arumalla", "cvv": 256, "cardexpiry": "2022-01"},
    {"buyername": "meghana", "totalamount": 534.9, "recipientname": "SBI Bank", "cradnumber": 2560123489892525, "nameoncard": "Arumalla", "cvv": 256, "cardexpiry": "2022-01"},
    {"buyername": "meghana", "totalamount": 35.0, "recipientname": "SBI Bank", "cradnumber": 5890123589745658, "nameoncard": "Susritha", "cvv": 247, "cardexpiry": "2022-01"},
    {"buyername": "bbb", "totalamount": 100.0, "recipientname": "Chase Bank", "cradnumber": 9870768546739998, "nameoncard": "bbb", "cvv": 435, "cardexpiry": "2022-12"},
]

for t in transactions:
    obj = BuyerTransactionModels.objects.create(**t)
    print(f"Transaction: {t['buyername']} → {t['recipientname']} ₹{t['totalamount']} (id={obj.id})")

# --- Blockchain Transactions ---
blockchain_txns = [
    {"c_sender": "harish", "c_recipient": "HDFC Bank", "c_amount": "50.0", "c_previous_hash": "38e7551d6e22862e889bbcf688ba339cdb5c840dbb8c412caa7b796194ac5e10", "c_index": "2", "c_timestamp": "1602325602.7917922", "c_proof": "100", "p_timestamp": "p_timestamp", "p_sender": "p_sender", "p_recipient": "p_recipient", "p_amount": "p_amount", "p_index": "1", "p_proof": "100", "p_previous_hash": "genesis"},
    {"c_sender": "harish", "c_recipient": "HDFC Bank", "c_amount": "300.0", "c_previous_hash": "9e03e15112b4a62cbd43149078bcc8d80c9e93da24e81519be5724226243f0ea", "c_index": "3", "c_timestamp": "1602325649.1655002", "c_proof": "100", "p_timestamp": "1602325602.7917922", "p_sender": "harish", "p_recipient": "HDFC Bank", "p_amount": "50.0", "p_index": "2", "p_proof": "100", "p_previous_hash": "38e7551d6e22862e889bbcf688ba339cdb5c840dbb8c412caa7b796194ac5e10"},
    {"c_sender": "ramesh", "c_recipient": "Canara Bank", "c_amount": "495.0", "c_previous_hash": "ae83dcd03eda83691aa254c9ce68231a29aaa297f2a43ad775475cfdcda07535", "c_index": "4", "c_timestamp": "1602325700.0", "c_proof": "100", "p_timestamp": "1602325649.1655002", "p_sender": "harish", "p_recipient": "HDFC Bank", "p_amount": "300.0", "p_index": "3", "p_proof": "100", "p_previous_hash": "9e03e15112b4a62cbd43149078bcc8d80c9e93da24e81519be5724226243f0ea"},
    {"c_sender": "ramesh", "c_recipient": "Canara Bank", "c_amount": "25.0", "c_previous_hash": "b79d3f83920ab7c4f7db34e8d2b60dc358b8b8c4add57138e798b85658e41cce", "c_index": "5", "c_timestamp": "1602325750.0", "c_proof": "100", "p_timestamp": "p_timestamp", "p_sender": "p_sender", "p_recipient": "p_recipient", "p_amount": "p_amount", "p_index": "4", "p_proof": "100", "p_previous_hash": "ae83dcd03eda83691aa254c9ce68231a29aaa297f2a43ad775475cfdcda07535"},
    {"c_sender": "meghana", "c_recipient": "SBI Bank", "c_amount": "534.9", "c_previous_hash": "958f8b110a19efef98570c691e1068933994cbabac89e5d8dd8aad39d07b3812", "c_index": "6", "c_timestamp": "1602329385.0400195", "c_proof": "100", "p_timestamp": "p_timestamp", "p_sender": "p_sender", "p_recipient": "p_recipient", "p_amount": "p_amount", "p_index": "5", "p_proof": "100", "p_previous_hash": "b79d3f83920ab7c4f7db34e8d2b60dc358b8b8c4add57138e798b85658e41cce"},
    {"c_sender": "meghana", "c_recipient": "SBI Bank", "c_amount": "534.9", "c_previous_hash": "62370fb334e5c713cc275187f2c49c09b1f3d03d9629fc7f6940f4fa560e83a4", "c_index": "7", "c_timestamp": "1602329385.4627755", "c_proof": "100", "p_timestamp": "1602329385.0400195", "p_sender": "meghana", "p_recipient": "SBI Bank", "p_amount": "534.9", "p_index": "6", "p_proof": "100", "p_previous_hash": "958f8b110a19efef98570c691e1068933994cbabac89e5d8dd8aad39d07b3812"},
    {"c_sender": "meghana", "c_recipient": "SBI Bank", "c_amount": "35.0", "c_previous_hash": "b90370042542617a9d526e8bf2020730129526ed8eb3d69a94fcc27c7121bc86", "c_index": "8", "c_timestamp": "1602329400.0", "c_proof": "100", "p_timestamp": "1602329385.4627755", "p_sender": "meghana", "p_recipient": "SBI Bank", "p_amount": "534.9", "p_index": "7", "p_proof": "100", "p_previous_hash": "62370fb334e5c713cc275187f2c49c09b1f3d03d9629fc7f6940f4fa560e83a4"},
    {"c_sender": "bbb", "c_recipient": "Chase Bank", "c_amount": "100.0", "c_previous_hash": "032df54b0893fbaa5677a171f3a25c8ab59809ada53a30e39d0190a03167ad2e", "c_index": "9", "c_timestamp": "1602329500.0", "c_proof": "100", "p_timestamp": "p_timestamp", "p_sender": "p_sender", "p_recipient": "p_recipient", "p_amount": "p_amount", "p_index": "8", "p_proof": "100", "p_previous_hash": "b90370042542617a9d526e8bf2020730129526ed8eb3d69a94fcc27c7121bc86"},
]

for bt in blockchain_txns:
    obj = BlockChainTransactionModel.objects.create(**bt)
    print(f"Blockchain txn: {bt['c_sender']} → {bt['c_recipient']} ₹{bt['c_amount']} (id={obj.id})")

# --- Buyer Cart (purchased items) ---
cart_items = [
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "alex", "cropname": "Tomato", "description": "A red Tomato For Health", "price": 25.0, "status": "purchased"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "alex", "cropname": "STRAWBERRY", "description": "A great Choice if you have", "price": 150.0, "status": "purchased"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "alex", "cropname": "Green Beans", "description": "Healthy Diet", "price": 95.0, "status": "purchased"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "sagar", "cropname": "CARROTS", "description": "Best For Health", "price": 89.9, "status": "purchased"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "alex", "cropname": "Tomato", "description": "A red Tomato For Health", "price": 25.0, "status": "purchased"},
    {"buyerusername": "harish", "buyeruseremail": "harishgangishetty@gmail.com", "sellername": "alex", "cropname": "Tomato", "description": "A red Tomato For Health", "price": 25.0, "status": "purchased"},
    {"buyerusername": "harish", "buyeruseremail": "harishgangishetty@gmail.com", "sellername": "alex", "cropname": "Tomato", "description": "A red Tomato For Health", "price": 25.0, "status": "purchased"},
    {"buyerusername": "ramesh", "buyeruseremail": "rameshsrc@gmail.com", "sellername": "alex", "cropname": "Green Beans", "description": "Healthy Diet", "price": 95.0, "status": "purchased"},
    {"buyerusername": "ramesh", "buyeruseremail": "rameshsrc@gmail.com", "sellername": "alex", "cropname": "STRAWBERRY", "description": "A great Choice if you have", "price": 150.0, "status": "purchased"},
    {"buyerusername": "ramesh", "buyeruseremail": "rameshsrc@gmail.com", "sellername": "sagar", "cropname": "BROCOLLI", "description": "A new Choice To Digest", "price": 250.0, "status": "purchased"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "alex", "cropname": "STRAWBERRY", "description": "A great Choice if you have", "price": 150.0, "status": "purchased"},
    {"buyerusername": "harish", "buyeruseremail": "harishgangishetty@gmail.com", "sellername": "alex", "cropname": "STRAWBERRY", "description": "A great Choice if you have", "price": 150.0, "status": "purchased"},
    {"buyerusername": "harish", "buyeruseremail": "harishgangishetty@gmail.com", "sellername": "alex", "cropname": "STRAWBERRY", "description": "A great Choice if you have", "price": 150.0, "status": "purchased"},
    {"buyerusername": "ramesh", "buyeruseremail": "rameshsrc@gmail.com", "sellername": "alex", "cropname": "Tomato", "description": "A red Tomato For Health", "price": 25.0, "status": "purchased"},
    {"buyerusername": "ramesh", "buyeruseremail": "rameshsrc@gmail.com", "sellername": "sagar", "cropname": "CARROTS", "description": "Best For Health", "price": 89.9, "status": "waiting"},
    {"buyerusername": "meghana", "buyeruseremail": "arumallameghana@gmail.com", "sellername": "sravani", "cropname": "Onion", "description": "A Maharstra onion", "price": 35.0, "status": "purchased"},
    {"buyerusername": "haseeb", "buyeruseremail": "mohdabdulhaseeb@gmail.com", "sellername": "adnan", "cropname": "Apple", "description": "100% Natural", "price": 100.0, "status": "waiting"},
    {"buyerusername": "haseeb", "buyeruseremail": "mohdabdulhaseeb@gmail.com", "sellername": "adnan", "cropname": "Apple", "description": "100% Natural", "price": 100.0, "status": "waiting"},
    {"buyerusername": "bbb", "buyeruseremail": "adnanuddin@gmail.com", "sellername": "aaa", "cropname": "Apple", "description": "100% Natural", "price": 100.0, "status": "purchased"},
]

for ci in cart_items:
    obj = BuyerCropCartModels.objects.create(**ci)
    print(f"Cart: {ci['buyerusername']} bought {ci['cropname']} ({ci['status']}) id={obj.id}")

print("\n✅ All sample data populated successfully!")
