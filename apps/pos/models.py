# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Model = models.Model


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Store update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Store(Model):
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.store_name


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Categorie update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Category(Model):
    id = models.AutoField(primary_key=True)
    category_id = models.CharField(max_length=255, blank=True)
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Items update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Item(Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price = models.DecimalField(max_digits=12,
                                     decimal_places=2)
    value = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                blank=True)
    reorder_level = models.DecimalField(max_digits=12,
                                        decimal_places=2,
                                        blank=True,
                                        default=10)
    reorder_quantity = models.DecimalField(max_digits=12,
                                           decimal_places=2,
                                           blank=True,
                                           default=10)

    location = models.CharField(max_length=255, blank=True, null=True)

    item_image = models.ImageField(default='item.png',
                                   upload_to='items/',
                                   null=True, blank=True)

    # Date relations
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # External relations
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 related_name='items')

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        self.value = float(self.quantity) * float(self.unit_price)

        super(Item, self).save(*args, **kwargs)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Stock update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Stock(Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='stock')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=12,
                                         decimal_places=2,
                                         blank=True)
    purchase_value = models.DecimalField(max_digits=12,
                                         decimal_places=2,
                                         blank=True)
    # how much profit per item base on sale and purchase price
    profit = models.DecimalField(max_digits=12,
                                 decimal_places=2,
                                 blank=True,
                                 default=0)
    # Date relations
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.item_name

    def save(self, *args, **kwargs):
        self.purchase_value = float(self.quantity) * float(self.purchase_price)
        self.profit = float(self.item.unit_price) - float(self.purchase_price)

        super(Stock, self).save(*args, **kwargs)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Dead Stock update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class DeadStock(Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='dead_stock')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=12,
                                         decimal_places=2,
                                         blank=True)
    loss = models.DecimalField(max_digits=12, decimal_places=2)
    # Date relations
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.item_name

    def save(self, *args, **kwargs):
        self.loss = float(self.quantity) * float(self.purchase_price)

        super(DeadStock, self).save(*args, **kwargs)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Sales update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Sale(Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='sales')
    description = models.TextField()
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    value = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                blank=True)

    # Date Relations
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    added_date = models.DateField(auto_now_add=True)
    added_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.description = f"{self.quantity} {self.item.item_name}(s) sold on {self.added_date} at {self.added_time}."

        super(Sale, self).save(*args, **kwargs)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Payments update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Payment(Model):
    # payment choices
    PAYMENT_METHOD_CHOICES = (
        ('KSH', 'CASH'),
        ('MP', 'MPESA'),
    )
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES,
                              default='KSH')
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    description = models.TextField()
    # Date relations
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    added_date = models.DateField(auto_now_add=True)
    added_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"A payment of '{self.amount}' made on {self.added_date} at {self.added_time}."


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Setting update model
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class UserSettings(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='settings')
    dark_mode = models.BooleanField(default=False)
    # Date relations
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Settings."
