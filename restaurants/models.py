from django.db import models
from transactions.models import CardRestaurantTransaction
from django.db.models import Sum
from decimal import Decimal

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=45)

    @property
    def balance(self):
        card_restaurant_sum = CardRestaurantTransaction.objects.filter(restaurant=self).aggregate(Sum('amount'))['amount__sum']
        if card_restaurant_sum is None:
            card_restaurant_sum = Decimal('0')
        return card_restaurant_sum

    def __str__(self):
        return f"{self.name}"
