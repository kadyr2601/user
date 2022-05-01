from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from products.models import Product
User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, related_name="user_cart", on_delete=models.CASCADE)
    total_price = models.IntegerField()
    discount_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(user=instance)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    children_count = models.IntegerField()
    adult_count = models.IntegerField()

    def __str__(self):
        return self.cart


class Order(models.Model):
    buyer = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    order_number = models.CharField(max_length=250, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.buyer.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_order", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=9, decimal_places=2)

    # @staticmethod
    # def create_order_item(order, product, quantity, total):
    #     order_item = OrderItem()
    #     order_item.order = order
    #     order_item.product = product
    #     order_item.quantity = quantity
    #     order_item.total = total
    #     order_item.save()
    #     return
