from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProductModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    picture = models.ImageField(upload_to='product_pics')
    description = models.TextField()
    is_avalible = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"