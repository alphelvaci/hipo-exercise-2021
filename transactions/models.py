from django.db import models

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
