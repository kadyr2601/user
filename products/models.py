from django.db import models
from categories.models import Category, SubCategory


class Coupon(models.Model):
    coupon = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.coupon


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_products')
    title = models.CharField(max_length=256)
    about = models.TextField()
    discount = models.IntegerField(default=None, blank=True, null=True)
    price = models.IntegerField()

    adult_price = models.IntegerField()

    children_price = models.IntegerField()
    discount_price = models.DecimalField(max_digits=9, decimal_places=2)
    partner_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title
