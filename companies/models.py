from django.db import models
from transactions.models import CompanyFundingTransaction, CompanyCardTransaction, CardRestaurantTransaction
from restaurants.models import Restaurant
from django.db.models import Sum
from django.core.exceptions import ValidationError
from decimal import Decimal

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return f"{self.name}"

    def list_cards(self):
        cards = []
        for employee in self.employee_set.all():
            cards.append(employee.card)
        return cards

    def list_top_restaurants(self):
        restaurant_popularity = []  # [(restaurant, transaction_count)]
        for restaurant in Restaurant.objects.all():
            transaction_count = CardRestaurantTransaction.objects.filter(card__employee__company=self, restaurant=restaurant, amount__gt=0).count()
            restaurant_popularity.append((restaurant, transaction_count))
        restaurant_popularity.sort(key=lambda x: x[1], reverse=True)  # sort by transaction_count
        return restaurant_popularity

    def add_funds(self, amount):
        transaction = CompanyFundingTransaction(company=self, amount=amount)
        transaction.save()


class Employee(models.Model):
    CONTRACT_TYPE_CHOICES = [
        ('small_town', 'Small Town'),
        ('city_center', 'City Center')
    ]

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    contract_type = models.CharField(max_length=15, choices=CONTRACT_TYPE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def create_card(self):
        if not hasattr(self, 'card'):  # has no card
            card = Card(employee=self)
            card.save()
        # maybe add an error message here

    def spend(self, restaurant, amount):
        if not hasattr(self, 'card'):
            raise Exception('Employee has no card!')
        if self.card.balance < amount:
            raise Exception('Balance insufficient!')
        transaction = CardRestaurantTransaction(card=self.card, restaurant=restaurant, amount=amount)
        transaction.save()


class Card(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT, null=True)
    terminated = models.BooleanField(default=False)

    @property
    def card_type(self):
        return self.employee.contract_type

    @property
    def balance(self):
        company_card_sum = CompanyCardTransaction.objects.filter(card=self).aggregate(Sum('amount'))['amount__sum']
        card_restaurant_sum = CardRestaurantTransaction.objects.filter(card=self).aggregate(Sum('amount'))['amount__sum']
        if company_card_sum is None:
            company_card_sum = Decimal('0')
        if card_restaurant_sum is None:
            card_restaurant_sum = Decimal('0')
        return company_card_sum - card_restaurant_sum

    def __str__(self):
        if not self.terminated:
            return f"{self.employee}'s Card (Card {self.id})"
        else:
            return f"Terminated Card (Card {self.id})"

    def clean(self):
        if (self.employee is None) != self.terminated:  # enforce if and only if (<->)
            raise ValidationError('Employee and terminated fields contradict!')

    def save(self, *args, **kwargs):
        try:
            self.clean()
            super(Card, self).save(*args, **kwargs)
        except ValidationError:
            raise Exception('Error saving: could not validate instance')

    def list_transactions(self):
        transactions = []
        for transaction in self.companycardtransaction_set.all():
            transactions.append(transaction)
        for transaction in self.cardrestauranttransaction_set.all():
            transactions.append(transaction)
        transactions.sort(key=lambda transaction: transaction.date)
        return transactions

    def terminate(self):
        if self.balance > 0:
            transaction = CompanyCardTransaction(card=self)
            transaction.amount = -self.balance  # transfer funds back to company
            transaction.save()
        if self.balance == 0:
            self.terminated = True
            self.employee = None
            self.save()
        else:
            raise Exception('Error!')
