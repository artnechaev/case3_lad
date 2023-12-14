from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveSmallIntegerField()
    date_updated = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name
