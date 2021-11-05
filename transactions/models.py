from django.db import models
from companies.models import Company, Card
from restaurants.models import Restaurant
from .helper_functions import get_amount_string

# Create your models here.


class Transaction(models.Model):  # any transaction
    amount = models.DecimalField(max_digits=11, decimal_places=2)  # up to 999 millon # TO-DO dont allow zero value
    date = models.DateTimeField()

    def __str__(self):
        return f"Transaction {self.id} ({get_amount_string(self)})"


class CompanyTransaction(models.Model):  # any company transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.company} Transaction {self.id} ({get_amount_string(self)})"


class CardTransaction(models.Model):  # any card transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.card} Transaction {self.id} ({get_amount_string(self)})"


class RestaurantTransaction(models.Model):  # any restaurant transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.restaurant} Transaction {self.id} ({get_amount_string(self)})"


# the following two models link transactions of two parties.
# this would be useful, for example when reversing a spending.
class CardTopup(models.Model):  # transaction between a company and a card
    company_transaction = models.OneToOneField(CompanyTransaction, on_delete=models.PROTECT)
    card_transactions = models.OneToOneField(CardTransaction, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.company_transaction.company}: {self.card_transactions.card} Topup {self.id} ({get_amount_string(self)})"



class CardSpending(models.Model):  # transaction between a card an a restaurant
    card_transactions = models.OneToOneField(CardTransaction, on_delete=models.PROTECT)
    restaurant_transactions = models.OneToOneField(RestaurantTransaction, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.card_transactions.card} Spending {self.id} at {self.restaurant_transactions.restaurant} ({get_amount_string(self)})"
