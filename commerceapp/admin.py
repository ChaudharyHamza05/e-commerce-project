from django.contrib import admin
from .models import ProductModel, PurchaseModel, SaleModel
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(PurchaseModel)
admin.site.register(SaleModel)