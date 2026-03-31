from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.views import View
from .forms import SignUpForm, ProductForm
from django.contrib.auth.forms import AuthenticationForm
from .models import ProductModel

#for signup view
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return  render(request, 'signup.html', {'form': form} )

#for login view
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return  render(request, 'login.html', {'form': form})
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'form': form})

#for logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
#===================================================================================

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return  render(request, 'home.html', {"user": request.user})


#create products view
class createproduct(LoginRequiredMixin, View):
    def get(self, request):
        product = ProductForm()
        return render(request, 'createproduct.html', {'product': product})

    def post(self, request):
        product = ProductForm(request.POST, request.FILES)
        if product.is_valid():
            product = product.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
        return render(request, 'createproduct.html', {'product': product})

class productlist(LoginRequiredMixin, View):
    def get(self, request):
        product = ProductModel.objects.all()
        return  render(request, 'productlist.html', {'product': product})

class productdetail(LoginRequiredMixin, View):
    def get(self, request, id):
        product = ProductModel.objects.get(id=id)
        return render(request, 'productdetails.html', {'product': product})

from django.shortcuts import get_object_or_404

class UpdateProduct(LoginRequiredMixin, View):
    def get(self, request, id):
        product = ProductModel.objects.get(id=id, user=request.user)
        form = ProductForm(instance=product)
        return render(request, 'updateproduct.html', {'form': form})

    def post(self, request, id):
        product = ProductModel.objects.get(id=id, user=request.user)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productdetail', id=id)
        return render(request, 'updateproduct.html', {'product': product, 'form': form})

class DeleteProduct(LoginRequiredMixin, View):
    def get(self, request, id):
        product = ProductModel.objects.get(id=id, user=request.user)
        product.delete()
        return redirect('productlist')