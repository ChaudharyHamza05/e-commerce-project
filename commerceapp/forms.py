from importlib.metadata import metadata
from pyclbr import Class

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProductModel, PurchaseModel, SaleModel

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'picture', 'description', 'is_avalible']

class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleModel
        fields = ['product', 'invoice_no', 'price', 'quantity', 'notes']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'invoice_no': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseModel
        fields = ['product', 'invoice_no', 'price', 'quantity', 'notes']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'invoice_no': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
