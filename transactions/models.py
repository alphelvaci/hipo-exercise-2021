from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class CompanyFundingTransaction(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)  # up to 999 millon
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError('Amount must be greater than zero!')

    def save(self, *args, **kwargs):
        try:
            self.clean()
            super(CompanyFundingTransaction, self).save(*args, **kwargs)
        except ValidationError:
            raise Exception('Error saving: could not validate instance')

    def __str__(self):
        return f"Funding {self.id} ({self.company} +{self.amount})"


class CompanyCardTransaction(models.Model):  # a positive amount implies a company to card transaction
    card = models.ForeignKey('companies.Card', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.card.terminated:
            raise ValidationError('This card is terminated!')
        if self.card.balance + self.amount < 0:
            raise ValidationError('Insufficient card balance!')
        if self.card.employee.company.balance - self.amount < 0:
            raise ValidationError('Insufficient company balance!')

    def save(self, *args, **kwargs):
        try:
            self.clean()
            super(CompanyCardTransaction, self).save(*args, **kwargs)
        except ValidationError:
            raise Exception('Error saving: could not validate instance')

    def __str__(self):
        if not self.card.terminated:
            return f"Transaction {self.id} ({self.card.employee.company} - {self.card} {self.amount})"
        else:
            return f"Transaction {self.id} ({self.card} {self.amount})"


class CardRestaurantTransaction(models.Model):  # a positive amount implies a card to restaurant transaction
    card = models.ForeignKey('companies.Card', on_delete=models.PROTECT)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.card.terminated:
            raise ValidationError('This card is terminated!')
        if self.card.balance - self.amount < 0:
            raise ValidationError('Insufficient card balance!')
        if self.restaurant.balance + self.amount < 0:
            raise ValidationError('Insufficient restaurant balance!')

    def save(self, *args, **kwargs):
        try:
            self.clean()
            super(CardRestaurantTransaction, self).save(*args, **kwargs)
        except ValidationError:
            raise Exception('Error saving: could not validate instance')

    def __str__(self):
        return f"Transaction {self.id} ({self.card} - {self.restaurant} {self.amount})"

    def refund(self):
        transaction = CardRestaurantTransaction(card=self.card, restaurant=self.restaurant)
        transaction.amount = -self.amount
        transaction.save()
