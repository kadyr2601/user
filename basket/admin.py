from django.contrib import admin
from basket.models import Cart, CartItem, OrderItem, Order

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order)
