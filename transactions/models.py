from django.db import models
from companies.models import Company, Card
from restaurants.models import Restaurant

# Create your models here.


class Transaction(models.Model):  # any transaction
    amount = models.DecimalField(max_digits=11, decimal_places=2)  # up to 999 millon # TO-DO dont allow zero value
    date = models.DateTimeField()

    def __str__(self):
        if self.amount < 0:
            amount_string = str(self.amount)
        else:
            amount_string = "+" + str(self.amount)
        return f"Transaction {self.id} ({amount_string})"


class CompanyTransaction(models.Model):  # any company transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.company} Transaction {self.id}"


class CardTransaction(models.Model):  # any card transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.card} Transaction {self.id}"


class RestaurantTransaction(models.Model):  # any restaurant transaction
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.restaurant} Transaction {self.id}"
