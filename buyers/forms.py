from django import forms
from buyers.models import BuyerUserRegistrationModel


class BuyerUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = BuyerUserRegistrationModel
        fields = ['name', 'loginid', 'password', 'mobile', 'email', 'locality', 'address', 'city', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'loginid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login ID'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Locality'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }
