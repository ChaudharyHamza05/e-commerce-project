from importlib.metadata import metadata
from pyclbr import Class

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProductModel

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'picture', 'description', 'is_avalible']
