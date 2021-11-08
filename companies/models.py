from django.db import models
from transactions.models import CompanyFundingTransaction
from django.utils import timezone

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

    def add_funds(self, amount):
        transaction = CompanyFundingTransaction(company=self, date=timezone.now(), amount=amount)
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


class Card(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)

    @property
    def card_type(self):
        return self.employee.contract_type

    def __str__(self):
        return f"{self.employee}'s Card (Card {self.id})"
