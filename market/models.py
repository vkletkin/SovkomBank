from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Name")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):

    sale_date = models.DateTimeField(
        auto_now_add=True, verbose_name="date of sale")
    quantity = models.PositiveIntegerField(default=1)
    name = models.ForeignKey(
        Product,  on_delete=models.CASCADE, related_name="Orders")
    price = Product.price
    total_price = models.FloatField(default = 0)

