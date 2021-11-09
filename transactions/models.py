from django.db import models
from django.utils import timezone

# Create your models here.


class CompanyFundingTransaction(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)  # up to 999 millon
    date = models.DateTimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(amount__gt=0), name='amount_gt_0'),
        ]

    def __str__(self):
        return f"Funding {self.id} ({self.company} +{self.amount})"


class CompanyCardTransaction(models.Model):  # a positive amount implies a company to card transaction
    card = models.ForeignKey('companies.Card', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()

    # todo constraint amount

    def __str__(self):
        if not self.card.terminated:
            return f"Transaction {self.id} ({self.card.employee.company} - {self.card} {self.amount})"
        else:
            return f"Transaction {self.id} ({self.card} {self.amount})"


class CardRestaurantTransaction(models.Model):  # a positive amount implies a card to restaurant transaction
    card = models.ForeignKey('companies.Card', on_delete=models.PROTECT)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField()

    # todo constraint amount

    def __str__(self):
        return f"Transaction {self.id} ({self.card} - {self.restaurant} {self.amount})"

    def refund(self):
        transaction = CardRestaurantTransaction(card=self.card, restaurant=self.restaurant, date=timezone.now())
        transaction.amount = -self.amount
        transaction.save()
