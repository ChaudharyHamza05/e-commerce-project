from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('createproduct/', createproduct.as_view(), name='createproduct'),
    path('updateproduct/<int:id>/', UpdateProduct.as_view(), name='updateproduct'),
    path('productlist/', productlist.as_view(), name='productlist'),
    path('productdetail/<int:id>/', productdetail.as_view(), name='productdetail'),
    path('deleteproduct/<int:id>/', DeleteProduct.as_view(), name='deleteproduct'),
]