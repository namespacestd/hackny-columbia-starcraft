from django.db import models
from django.contrib.auth.models import User

import logging

logger = logging.getLogger('root.' + __name__)

class UserAccount(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    reliability = models.IntegerField()

class SellerItem(models.Model):
    DINING_HALLS = (
        ('john-jay', 'john-jay'),
        ('ferris', 'ferris'),
        ('jjs', 'jjs'),
    )

    price = models.FloatField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    dining_hall = models.CharField(max_length=15, choices=DINING_HALLS, default='john-jay')
    is_sold = models.BooleanField(default=False)
    user = models.ForeignKey(UserAccount)

class Transaction(models.Model):
    PAYMENT_OPTION = (
        ('cash', 'cash'),
        ('paypal', 'paypal'),
    )
    meal = models.ForeignKey(SellerItem)
    buyer = models.ForeignKey(UserAccount)
    payment_option = models.CharField(max_length=15, choices=PAYMENT_OPTION, default='cash')
    designated_time = models.TimeField()
    paid = models.BooleanField(default=False)